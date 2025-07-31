import re
import json

origin = """00:00 好了，那我们紧接着第三圈，
00:02 第二个镜头，
00:03 也就是B组摄像机的B3这一段。⏹
00:07 在这一次我们写到周围群像的
00:09 时候，我们不只是写一致性，
00:11 也不只是写分区分组，
00:13 我们还要找到其中一些很有个性的点，⏹
00:16 比如我们在画面中寻找点面结合中
00:18 的这个所谓的点，
00:20 这个点可以是人，
00:21 也可以是某个事物。⏹
00:24 只要它很突出，
00:26 它很有个性啊，
00:27 就值得我们去描写。⏹
00:29 而这个个性最好跟你。
00:31 本篇文章要写的主题还要有呼应。⏹
00:34 举个例子，
00:35 如果在下雨天，
00:36 我们用这样的场景描绘危险时人民
00:40 子弟兵冲锋在前，⏹
00:42 风雨中有人民在他身后守护，
00:45 两者之间共命运的深情。⏹
00:48 执勤的士兵。
00:51 他喉结滚动，
00:52 想说些什么。⏹
00:54 却只见雨水正从老人佝偻的肩头淌
00:57 下，在洗得发白的旧中山装上印出了
01:01 深色的痕迹。⏹
01:02 他绷紧的下颌线突然一颤，
01:04 滚烫的液体就着雨水滑进衣领，⏹
01:07 但那伞始终稳稳地向着军徽倾斜
01:12 着。⏹
01:13 再比如说，
01:14 一名刚入伍不久的新兵，
01:16 胸膛绷得像要炸开，⏹
01:18 喉结在紧抿的唇线下剧烈地滚动了
01:22 一下，挺得笔直的脊背。
01:24 微微的发僵，⏹
01:25 唯有那双年轻的眼睛灼灼燃烧着
01:28 近乎神圣的光芒，
01:30 死死锁住上升的旗脚。⏹
01:33 这样的描写就可以更加的放大周围
01:36 环境的特点，
01:37 尤其是这些有个性的点。⏹"""
lines = [
    "{01:23 hello world ⏹}",
    "{02:25 nihao}",
    "{02:34 another line ⏹}",
    "{03:45 something else ⏹}"
]

result = []
judge = False
for line in origin.splitlines():
    match = re.match(r"(\d{2,}):(\d{2})\s+([^\}]+)⏹", line)
    match2 = re.match(r"(\d{2,}):(\d{2})\s+([^\}]+)", line)
    if judge and match2:
        minutes = int(match2.group(1))
        seconds = int(match2.group(2))
        total_seconds = minutes * 60 + seconds
        total_mseconds = total_seconds * 1000
        text = match2.group(3).strip()
        result.append({
            "time": total_mseconds})
        judge = False
    if match:
        judge = True
        continue

print(json.dumps(result, ensure_ascii=False, indent=2))
