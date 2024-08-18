import base64
import glob
import os
import sys
import urllib.parse


def url_encode(tgt: str) -> str:
    quote = urllib.parse.quote(tgt)

    return quote


def convert_bytes2base64(bytes: bytes) -> bytes:
    bytes_base64 = base64.b64encode(bytes)

    return bytes_base64


def convert_img2str(img_path: str) -> str:
    with open(img_path, "rb") as f:
        img_bytes = f.read()

    bytes_base64 = convert_bytes2base64(img_bytes)
    str_base64 = bytes_base64.decode()
    return str_base64


class ArgInfo:
    html_file_path_m: str = ""
    img_folder_path_m: str = ""

    def __init__(self) -> None:
        pass

    def check_argv(self) -> bool:
        if len(sys.argv) < 3:
            print("引数で入力ファイルを指定してください。")
            print("引数1: 変換したいhtmlファイル")
            print("引数2: 画像ファイルの配置されたフォルダパス")
            return False

        html_file_path = sys.argv[1]
        if os.path.isfile(html_file_path) is False:
            print(f"存在するファイルを指定してください。\r\n現在の指定パス: {html_file_path}")
            return False

        if html_file_path.endswith(".html") is False:
            print(f"htmlファイルを指定してください。\r\n現在の指定パス: {html_file_path}")
            return False

        img_folder_path = sys.argv[2]
        if os.path.isdir(img_folder_path) is False:
            print(f"存在するフォルダを指定してください。\r\n現在の指定パス: {img_folder_path}")
            return False

        img_file_path_list = glob.glob(f"{img_folder_path}\\**\\*.*", recursive=True)
        if len(img_file_path_list) == 0:
            print(f"画像ファイルが存在しません。\r\n現在の指定パス: {img_folder_path}")
            return False

        self.html_file_path_m = html_file_path
        self.img_folder_path_m = img_folder_path
        self.img_file_path_list_m = img_file_path_list
        return True

    def output_file_name(self) -> str:
        file_path, file_name = os.path.split(self.html_file_path_m)
        name, ext = file_name.split(".")
        return f"{file_path}\\{name}_rep.{ext}"

    def convert_image_info_list(self) -> list[list[str]]:
        image_info_list = []
        for img_file_path in self.img_file_path_list_m:
            # 画像のファイル名をパーセントエンコードする
            img_file_name_encoded_url = url_encode(os.path.basename(img_file_path))
            tgt_pattern = f'/{img_file_name_encoded_url}" alt="'

            # 画像をbase64形式に変換して埋め込む
            img_file_converted_str = convert_img2str(img_file_path)
            rep_str = f'<p><img src="data:image/png;base64,{img_file_converted_str}" /></p>'
            image_info_list.append([tgt_pattern, rep_str])

        return image_info_list


def main() -> None:
    # 引数チェック
    arg_info = ArgInfo()
    if arg_info.check_argv() is False:
        return

    # htmlファイルの読み込み
    with open(arg_info.html_file_path_m, encoding="utf-8") as f:
        tgt_html_lines = f.readlines()

    # htmlファイル内の画像をURIからbase64に置換する
    img_info_list = arg_info.convert_image_info_list()
    for cnt, tgt_html_line in enumerate(tgt_html_lines):
        for img_info in img_info_list:
            if img_info[0] in tgt_html_line:
                tgt_html_lines[cnt] = img_info[1]
                break

    # 画像を埋め込んだhtmlファイルの保存
    with open(arg_info.output_file_name(), "w", encoding="utf-8") as f:
        f.writelines(tgt_html_lines)


if __name__ == "__main__":
    sys.argv.append(r"path\to\html\file\xxx.html")
    sys.argv.append(r"path\to\img\folder")
    main()
