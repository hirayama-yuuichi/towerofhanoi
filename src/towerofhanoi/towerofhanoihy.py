"""タワー オブ ハノイ　Hirayama.yuuichi hirayama.yuuichi@gmail.com
円盤のタワーを別の場所にを移動する遊び。ただし、大きい円盤を小さい円盤の上に置くことは出来ない。

"""

"""
変更した
"""


import sys

TOTAL_DISKS = 3  # 円盤の数

# SOLVED_TOWER=[x for x in range(TOTAL_DESKS,-1,-1) ] #正解の塔のイメージ
SOLVED_TOWER = list(range(TOTAL_DISKS, 0, -1))  # 正解の塔のイメージ


def main():
    """タワーオブハノイを１回実行する"""

    towers = {"A": SOLVED_TOWER, "B": [], "C": []}

    while True:

        # ゲーム版の表示
        displayTower(towers)

        # ユーザの入力を取得する。
        fromTower, toTower = getPlayerMove(towers)

        # DISKを移動する。
        oneDisk = towers[fromTower].pop()
        towers[toTower].append(oneDisk)

        # 終了判定
        if SOLVED_TOWER in (towers["B"], towers["C"]):
            displayTower(towers)
            print("win")
            sys.exit()


def getPlayerMove(towers):
    """正しい値か[QUIT]が入力されるまでプレーヤから入力を受け取る"""

    while True:
        print(
            """AB AC BA BC CA CBで移動方法を入力してください
    ABと入力した場合DISKをA->Bに移動します。
    終了の場合は[QUIT]と入力してください。
    """
        )
        response = input("> ").upper().strip()

        if response == "QUIT":
            print("ゲームを終了します。")
            sys.exit()

        # 入力文字が正しいか判定する
        if response not in ("AB", "AC", "BA", "BC", "CA", "CB"):
            continue  # 入力内容が正しくないので再入力を求める

        # 解りやすい名前にする
        # fromTower,toTower = responseでもOKだが、こちらの方が分かり易い
        fromTower, toTower = response[0], response[1]

        # 最大個数積んである塔には移動できない
        if len(towers[fromTower]) == 0:
            continue  # 入力内容が正しくないので再入力を求める

        # 0個積んである塔には移動できる
        elif len(towers[toTower]) == 0:
            return fromTower, toTower

        # 移動元のdiskより移動先のdiskが大きい時は移動できない。
        elif towers[fromTower][-1] >= towers[toTower][-1]:
            continue  # 入力内容が正しくないので再入力を求める
        else:
            return fromTower, toTower


def displayTower(towers):
    print("")
    for level in range(TOTAL_DISKS, 0, -1):
        levelString = []
        for tower in towers.values():

            if len(tower) < (level):
                levelString.append(" " * TOTAL_DISKS + " | |" + " " * TOTAL_DISKS)
            else:
                diskSize = tower[level - 1]  # 配列は-1する:
                levelString.append(
                    "{}{}{}| |{}{}".format(
                        " " * (TOTAL_DISKS - diskSize),
                        "@" * diskSize,
                        str(diskSize),
                        "@" * diskSize,
                        " " * (TOTAL_DISKS - diskSize),
                    )
                )
        print(*levelString)


# このプログラムが単体で実行された（inportされずに）場合実行します
if __name__ == "__main__":
    main()
