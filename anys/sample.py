import base64
import urllib.parse


def sample_encode(tgt: str) -> str:
    quote = urllib.parse.quote(tgt)
    print(f"Tgt: {tgt},\t Enc: {quote}")

    return quote


def sample_decode(tgt: str) -> str:
    unquote = urllib.parse.unquote(tgt)
    print(f"Tgt: {tgt},\t Dec: {unquote}")

    return unquote


def sample_bytes2base64(bytes: bytes) -> bytes:
    bytes_base64 = base64.b64encode(bytes)
    print(bytes_base64)

    return bytes_base64


def sample_img2str(img_path: str) -> str:
    with open(img_path, "rb") as f:
        img_bytes = f.read()

    bytes_base64 = sample_bytes2base64(img_bytes)
    str_base65 = bytes_base64.decode()
    return str_base65


def main() -> None:
    str_quote = sample_encode("画像テスト.png")
    sample_decode(r"%E7%94%BB%E5%83%8F%E3%83%86%E3%82%B9%E3%83%88.png")
    bytes_img = sample_img2str(r"D:\\work\\Otr\\02aboutGit\\img\\画像テスト.png")

    file_name = "aboutGit.html"
    base_path = r"D:\\work\\Otr\\02aboutGit\\"
    tgt_html = base_path + file_name
    with open(tgt_html, encoding="utf-8") as f:
        tgt_html_lines = f.readlines()

    tgt_str = f'<p><img src="./img/{str_quote}" alt="test"></p>'
    rep_str = f'<p><img src="data:image/png;base64,{bytes_img}" /></p>'

    for cnt, tgt_html_line in enumerate(tgt_html_lines):
        if tgt_str in tgt_html_line:
            print(tgt_html_line)
            tgt_html_lines[cnt] = rep_str

    rep_html = base_path + "rep_" + file_name
    with open(rep_html, "w", encoding="utf-8") as f:
        f.writelines(tgt_html_lines)


if __name__ == "__main__":
    main()
