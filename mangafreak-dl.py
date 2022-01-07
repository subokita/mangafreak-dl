#! /usr/bin/env python
# -*- coding: utf-8 -*-

import ujson
from pprint     import pprint
from halo       import Halo
from subprocess import call, run, check_output

def read_json():
    with open( "data.json", 'r' ) as file:
        data = ujson.load( file )
        return data

def write_json( data ):
    with open( "data.json", "w" ) as file:
        file.write( ujson.dumps( data, indent = 4 ) )
        pass
    return


def check_download_exist( url ):
    res = run( ["wget", "--spider", url ], capture_output = True )
    return not "Length: unspecified" in res.stderr.decode( 'utf-8' )


def main():
    spinner  = Halo( text = "", spinner = 'dots' )
    data     = read_json()
    url_stem = "http://images.mangafreak.net:8080/downloads"

    for key, values in data.items():
        slug         = values['slug']
        last_chapter = values['last_chapter']
        next_chapter = last_chapter + 1

        while True:
            url         = f'{url_stem}/{slug}_{next_chapter}'
            output_file = f'./temp/{key} c{next_chapter:03}.cbz'

            spinner.start( f"Checking {key:21} for chapter {next_chapter:4}" )
            if check_download_exist( url ):
                spinner.stop()

                command = ["wget", "-q", "-c", url, "-O", output_file, '--show-progress', '--limit-rate=1500K']
                call( command )
                next_chapter = next_chapter + 1
                pass

            else:
                values['last_chapter'] = next_chapter - 1
                break

            continue

        continue

    write_json( data )
    spinner.stop()

    call( ['osascript', '-e', 'display notification "DONE" with title "Manga" sound name "Purr"'] )

    print('[DONE]')
    return

if __name__ == '__main__':
    main()