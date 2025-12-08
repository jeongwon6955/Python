# 파일 처리 p190
'''
f = open("file2.txt", "w") # 쓰기 모드

f.write("hello")
f.write("\n")
f.write("안녕하십니까 저는 ai1한년 1반 최정원입니다 제가 기능반을 하면서 실무를 경험 해보고 싶어 이 도제 면접에 참여하게 되었습니다")
f.close()

f = open("file2.txt", "a") # 추가 모드
f.write("\n")
f.write("저는 도제를 미래인제 양성의 길이라고 생각합니다 도제를 통해 남들보다 먼저 사회생활을 경험하고 그를 바탕으로 사회에 기여 할 수 있는 사람으로 성장 할 수 있기 때문입니다")
f.close()


f = open("file.txt", "r") # 읽기 모드

w = f.read(200)
print(w)

f.close()
'''

f = open('live.txt', "wt")
f.write('''삶이 그대를 속일지라도 
슬퍼하거나 노하지 말라!
우울한 날들을 견디며
믿으라, 기쁨의 날이 오리니
''')
f.close()

# 파일 내용앞에 일련번호 붙이기

f = open("live.txt", 'rt')
text = ""
line = 1
while True:
    row = f.readline()
    if not row:
        break
    text += str(line) + ":" + row
    line += 1
f.close()
print(text)