import re
import json

origin = """00:00 你准备好了吗？
00:01 下面我们开始第三圈的指导。⏹
00:04 首先第三圈的第一个镜头。
00:07 我们已经给了特写和中景了，
00:09 那么这一次呢？
00:10 我们要相对给一个远的镜头，⏹
00:13 镜头得向后拉伸，
00:14 让读者能够感受到这种拉伸的
00:17 效果。所以在观察者和描写对象之间，
00:19 我们也可以增加一些遮挡物和
00:22 隔离。⏹
00:23 也可以利用一些光影来制造氛围。⏹
00:26 来我们举例A3这一段。⏹
00:29 比如在升旗仪式上，
00:31 他的身影如同一张绷紧的硬弓敬
00:34 立，整个身影沉稳如山，⏹
00:37 稳稳前倾的态势蓄满了千钧的
00:40 力气。⏹
00:41 或者写整个身影已与脚下的广场
00:44 融为一体，
00:45 挺拔的躯干化为托举旗帜升腾的
00:48 伟大力量。⏹
00:50 这力量从大地深处奔腾，
00:52 穿过他的身体。⏹
00:55 再比如，
00:56 金色的光芒度量了他刚毅的轮廓，⏹
00:59 绷直如铁的线条，
01:01 奋力向上的姿态，
01:02 熔铸成了一尊顶天立地的金色
01:06 塑像。⏹"""
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
        text = match2.group(3).strip()
        result.append({
            "time": total_seconds})
        judge = False
    if match:
        judge = True
        continue

print(json.dumps(result, ensure_ascii=False, indent=2))
