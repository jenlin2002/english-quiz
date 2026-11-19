"""單字區投影片改用單字卡的音檔（2026-11-20）。

投影片每個 🔊 原本各有一個 audio/uNN/slide-NN.mp3，但唸的內容和單字卡的 w-NN（單字）、e-NN（例句）一模一樣，
整個網站的檔案數因此超過 Cloudflare Pages 的 20000 個上限。這裡把投影片按鈕加上 data-src 指到單字卡那份音檔，
投影片的播放程式（slides_tail.html）有 data-src 就用它，沒有才用 slide-NN.mp3。

用法：python tools/vocab_gen/link_slide_audio.py [--delete]   處理 vocab/*/uNN-slides.html；--delete 刪掉不再用到的 slide-NN.mp3
build_vocab.py 產生投影片時也會呼叫 link()，所以新單元不會再錄重複的 slide 音檔。
"""
import glob, html, os, re, sys

BTN = re.compile(r'<button class="sentence-btn" type="button" data-say="([^"]*)"')
OLD_PLAY = "const a = new Audio('audio/"
NEW_PLAY = "const a = new Audio(btn.getAttribute('data-src') || 'audio/"


def card_map(card_html):
    """單字卡頁：唸的文字 → 音檔路徑（相對於單元資料夾）。"""
    m = {}
    for src, say in re.findall(r'data-src="([^"]*)" data-say="([^"]*)"', card_html):
        m.setdefault(html.unescape(say), src)
    return m


def link(page, cmap):
    """回傳 (新的投影片 HTML, 還要用 slide-NN.mp3 的 [(第幾個按鈕, 文字)])。"""
    keep = []
    n = [0]

    def rep(mo):
        n[0] += 1
        say = html.unescape(mo.group(1))
        src = cmap.get(say)
        if src:
            return '<button class="sentence-btn" type="button" data-src="%s" data-say="%s"' % (src, mo.group(1))
        keep.append((n[0], say))
        return mo.group(0)

    page = BTN.sub(rep, page)
    if OLD_PLAY in page and NEW_PLAY not in page:
        page = page.replace(OLD_PLAY, NEW_PLAY, 1)
    return page, keep


def main(delete):
    root = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', '..'))
    removed = 0
    for p in sorted(glob.glob(os.path.join(root, 'vocab', '*', 'u*-slides.html'))):
        d, tag = os.path.dirname(p), os.path.basename(p)[:3]
        with open(os.path.join(d, tag + '.html'), encoding='utf-8') as f:
            cmap = card_map(f.read())
        with open(p, encoding='utf-8', newline='') as f:
            old = f.read()
        new, _ = link(old, cmap)
        btns = re.findall(r'<button class="sentence-btn"[^>]*>', new)
        keep = [(i + 1, b) for i, b in enumerate(btns) if 'data-src=' not in b]
        if new != old:
            with open(p, 'w', encoding='utf-8', newline='') as f:
                f.write(new)
        need = {'slide-%02d.mp3' % i for i, _ in keep}
        adir = os.path.join(d, 'audio', tag)
        extra = [x for x in glob.glob(os.path.join(adir, 'slide-*.mp3')) if os.path.basename(x) not in need]
        print('%s/%s：投影片按鈕改用單字卡音檔，剩 %d 個 slide 音檔要用，%d 個可刪'
              % (os.path.basename(d), tag, len(need), len(extra)))
        if delete:
            for x in extra:
                os.remove(x)
                removed += 1
    if delete:
        print('刪掉 %d 個 slide 音檔' % removed)


if __name__ == '__main__':
    main('--delete' in sys.argv)
