import argparse
from pytube import YouTube, Playlist
from ffmpeg import _ffmpeg


def convert(file_path: str):
    dot = file_path.rfind('.')
    mp3_file = file_path[:dot] + '.mp3'
    converter = _ffmpegmpeg().input(file_path).output(mp3_file)
    converter.execute()

def download(args):
    urls = Playlist(args.url) if args.playlist else [args.url]
    for url in urls:
        print(f'Downloading {url}')
        yt = YouTube(url)
        stream = yt.streams.filter(
            progressive=True,
            file_extension=args.extension,
            ).order_by('resolution').desc().first()
        if stream is None:
            continue
        print(stream)
        file_path = stream.download(
            output_path=args.output_dir,
            filename=None if args.filename is None else f"{args.filename}.{args.extension}"
        )
        print(f'Convering {file_path} to mp3')
        convert(file_path)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Download youtube video'
    )
    parser.add_argument('url', type=str)
    parser.add_argument('--output-dir', '-o', type=str, default=None)
    parser.add_argument('--filename', '-f', type=str, default=None)
    parser.add_argument(
        '--extension',
        '-e',
        choices=['mp4'],
        default='mp4'
    )
    parser.add_argument('--playlist', '-p', action='store_true')


    args = parser.parse_args()

    download(args)
