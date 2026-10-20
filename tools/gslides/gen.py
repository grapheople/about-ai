import json, sys
F="Noto Sans KR"; MONO="Roboto Mono"
INK="#1F2937"; MUTED="#6B7280"; ACC="#EA580C"; TINT="#FFF1E8"; CARD="#F3F4F6"; DARK="#111827"; LIGHT="#F9FAFB"; ACC2="#FDBA74"
slides=[]; bg={}
def T(i,role): return f"s{i:02d}_{role}"
def title(i,text,h=1.1):
    return {"id":T(i,"title"),"type":"text","x":0.5,"y":0.35,"w":9,"h":h,"text":text,"size":28,"bold":True,"color":INK,"font":F}
def txt(i,role,x,y,w,h,text,size=18,**kw):
    d={"id":T(i,role),"type":"text","x":x,"y":y,"w":w,"h":h,"text":text,"size":size,"color":kw.pop("color",INK),"font":kw.pop("font",F)}; d.update(kw); return d
def card(i,role,x,y,w,h,text,size=18,fill=CARD,color=INK,**kw):
    d={"id":T(i,role),"type":"round_rect","x":x,"y":y,"w":w,"h":h,"fill":fill,"text":text,"size":size,"color":color,"font":kw.pop("font",F)}; d.update(kw); return d
def S(i,els,dark=False):
    slides.append({"id":T(i,"slide"),"layout":"BLANK","elements":els}); bg[T(i,"slide")]=DARK if dark else "#FAFAFA"
def lead(i,main,sub=None,foot=None,size=36):
    els=[txt(i,"main",0.75,1.3 if sub else 1.7,8.5,1.6,main,size,bold=True,color=LIGHT,align="CENTER")]
    if sub: els.append(txt(i,"sub",0.75,3.05,8.5,0.9,sub,20,color=ACC2,align="CENTER"))
    if foot: els.append(txt(i,"foot",0.75,4.1,8.5,0.6,foot,16,color="#D1D5DB",align="CENTER"))
    S(i,els,True)
def prompt(i,y,text,h=1.2,size=16):
    return card(i,"prompt",0.5,y,9,h,text,size,fill=TINT,color=INK)

lead(1,"현지에서 한 문장,\n여행 계획 전체가 바뀐다",size=40)
lead(2,"기억하는 여행 계획 만들기","Claude × Obsidian으로 시작하는 LLM 위키","L1-01",size=40)
S(3,[title(3,"저는 요즘 코드를 한 줄도 직접 짜지 않습니다"),
  card(3,"c1",0.5,1.8,2.85,2.6,"커머스 플랫폼\n개발자",20,align="CENTER",bold=True),
  card(3,"c2",3.575,1.8,2.85,2.6,"개발은\n전부 AI",20,fill=ACC,color="#FFFFFF",align="CENTER",bold=True),
  card(3,"c3",6.65,1.8,2.85,2.6,"나의 일\n무엇을 만들지 정하고\n판단하기",18,align="CENTER")])
S(4,[title(4,"AI의 일은 개발을 넘어섰다"),
  card(4,"c1",0.5,1.9,2.0,1.6,"개발",24,fill=ACC,color="#FFFFFF",bold=True,align="CENTER"),
  card(4,"c2",2.833,1.9,2.0,1.6,"기획",24,fill=TINT,bold=True,align="CENTER"),
  card(4,"c3",5.166,1.9,2.0,1.6,"QA",24,fill=TINT,bold=True,align="CENTER"),
  card(4,"c4",7.5,1.9,2.0,1.6,"디자인",24,fill=TINT,bold=True,align="CENTER"),
  txt(4,"cap",0.5,3.85,9,0.6,"처음엔 개발만. 지금은 기획, QA, 디자인까지 AI와 함께.",18,color=MUTED)])
S(5,[title(5,"20명이 하던 프로젝트를 5명이 합니다"),
  txt(5,"big",0.5,1.7,4.6,1.6,"20명 → 5명",54,bold=True,color=ACC),
  txt(5,"bigcap",0.5,3.3,4.6,0.5,"같은 규모의 프로젝트",16,color=MUTED),
  card(5,"bible",5.4,1.7,4.1,2.4,"모든 소통의 기준\nAI가 쓴 \"바이블\" 기획서",20,fill=TINT,bold=True,align="CENTER")])
lead(6,"그 방식을,\n오늘 여러분의 여행에 씁니다","AI가 쓰고, AI가 고치고, 사람은 판단한다")
S(7,[title(7,"오늘 할 것",0.8),
  card(7,"c1",0.5,1.35,2.85,1.9,"1\n프로그램 3개 설치",20,bold=True,align="CENTER"),
  card(7,"c2",3.575,1.35,2.85,1.9,"2\nAI와 함께\n위키 규칙 만들기",20,bold=True,align="CENTER"),
  card(7,"c3",6.65,1.35,2.85,1.9,"3\n여행 계획 짜고,\n바꿔 보기",20,bold=True,align="CENTER"),
  txt(7,"prep",0.5,3.6,9,0.5,"준비물: Mac, Claude Pro 이상 (월 $20, 촬영 시점 기준)",18,bold=True),
  txt(7,"win",0.5,4.15,9,0.5,"Windows 사용자는 설명란의 안내를 참고하세요",16,color=MUTED)])
S(8,[title(8,"채팅으로 짠 계획은 대화가 끝나면 사라진다"),
  card(8,"b1",0.5,1.7,5.2,0.75,"\"도쿄 3박 4일 짜 줘\"",18),
  card(8,"b2",1.6,2.65,5.6,0.75,"며칠 뒤 \"아이가 6살이라 많이 못 걷는데\"",18),
  txt(8,"res",0.5,3.75,9,0.7,"→ 처음부터 다시 설명",26,bold=True,color=ACC)])
S(9,[title(9,"위키는 쌓이고, 바뀔 때 같이 바뀐다"),
  {"id":T(9,"table"),"type":"table","x":0.5,"y":1.6,"w":9,"size":16,"font":F,"color":INK,
   "rows":[["문서 올려서 묻기","LLM 위키"],["질문마다 처음부터 다시 찾기","정리해서 파일로 남김"],["아무것도 안 쌓임","장소마다 페이지, 서로 연결"],["","새 정보가 오면 관련 페이지를 함께 수정"]],
   "header":True,"col_widths":[4.0,5.0],"row_h":0.5},
  txt(9,"key",0.5,4.25,9,0.6,"대화는 사라지지만, 위키는 쌓인다",24,bold=True,color=ACC)])
S(10,[title(10,"사람은 질문하고, AI는 정리한다"),
  {"id":T(10,"table"),"type":"table","x":0.5,"y":1.6,"w":4.6,"size":18,"font":F,"color":INK,
   "rows":[["사람","AI"],["자료 고르기","요약"],["질문하기","연결"],["방향 정하기","고치기"]],"header":True,"row_h":0.55},
  card(10,"quote",5.5,1.6,4.0,2.3,"\"Obsidian은 작업 화면,\nAI는 일하는 사람,\n위키는 결과물\"",18,fill=TINT,align="CENTER"),
  txt(10,"src",5.5,4.0,4.0,0.4,"안드레 카파시의 비유",14,color=MUTED,align="CENTER")])
lead(11,"설치 ① Obsidian","무료, 드래그 한 번","볼트 이름: travel-wiki")
lead(12,"설치 ② 생애 첫 터미널","Cmd + Space → Terminal → Enter","오늘 터미널은 여기가 처음이자 마지막")
S(13,[title(13,"명령 한 줄 → claude → 로그인"),
  card(13,"code",0.5,1.6,9,0.8,"curl -fsSL https://claude.ai/install.sh | bash",18,fill=DARK,color=LIGHT,font=MONO),
  txt(13,"steps",0.5,2.7,9,2.2,"설치 중엔 아무 표시가 없습니다. 기다리세요\n\"Claude Code successfully installed!\" 확인 후 claude 입력, 브라우저에서 로그인\ncommand not found: claude 가 나오면 새 터미널 창에서 다시",18,bullets=True,space_below=8)])
lead(14,"설치 ③ Claudian","설정 → 커뮤니티 플러그인 → Claudian 검색 → 설치 → 활성화","왼쪽엔 노트, 오른쪽엔 AI")
S(15,[title(15,"AI와 함께 위키 규칙 만들기"),
  prompt(15,1.55,"https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f\n이 글을 읽고, 이 볼트를 내 여행 계획용 LLM 위키로 만들어 줘.\n필요한 건 나한테 물어봐.",1.4,15),
  txt(15,"res",0.5,3.2,9,0.5,"→ CLAUDE.md, 폴더, 내 여행 취향 프로필",20,bold=True),
  txt(15,"note",0.5,3.9,9,0.5,"화면이 저와 조금 달라도 정상입니다",18,color=ACC,bold=True)])
S(16,[title(16,"자료를 넣으면, 페이지가 생기고 연결된다"),
  prompt(16,1.55,"이 문서를 위키에 추가해 줘: ko.wikipedia.org/wiki/아사쿠사\n이것도: ko.wikipedia.org/wiki/긴자",1.1,16),
  txt(16,"res",0.5,3.0,9,0.9,"→ 요약, 도쿄, 동네, 명소 페이지가 생기고 서로 연결\n→ 그래프 뷰에서 점과 선으로 확인",20,bold=True)])
S(17,[title(17,"위키를 근거로 계획이 나온다"),
  prompt(17,1.55,"6월에 가족이랑 3박 4일 도쿄 여행 계획 짜줘.\n동행자는 6세 아이와 아내 둘이야.",1.1,16),
  txt(17,"pts",0.5,2.95,9,1.8,"6살 아이에 맞춰 걷는 거리를 줄이고 쉬는 시간 추가\n내 취향 프로필 반영\n아사쿠사, 긴자 페이지로 링크",18,bullets=True,space_below=8)])
S(18,[title(18,"실화: 날이 좋아서 계획을 바꿨다"),
  card(18,"before",0.5,1.7,4.3,1.8,"원래 계획\n둘째 날 실내 전시",20,align="CENTER"),
  card(18,"after",5.2,1.7,4.3,1.8,"현지에서\n수상버스 타고 도쿄타워 쪽으로",20,fill=ACC,color="#FFFFFF",bold=True,align="CENTER"),
  txt(18,"key",0.5,3.85,9,0.6,"문제는 바뀐 다음",24,bold=True,color=ACC)])
S(19,[title(19,"한 문장으로 재현"),
  prompt(19,1.5,"지금 여행 둘째 날이야. 날씨가 너무 좋아서 실내 일정 대신\n수상버스 타고 도쿄타워 쪽으로 가고 싶어. 계획 바꿔 줘.",1.1,16),
  card(19,"k1",0.5,2.95,2.1,1.4,"일정",18,fill=TINT,bold=True,align="CENTER"),
  card(19,"k2",2.8,2.95,2.1,1.4,"점심\n식당 후보",18,fill=TINT,bold=True,align="CENTER"),
  card(19,"k3",5.1,2.95,2.1,1.4,"새 장소\n페이지",18,fill=TINT,bold=True,align="CENTER"),
  card(19,"k4",7.4,2.95,2.1,1.4,"걷는 거리\n재확인",18,fill=TINT,bold=True,align="CENTER")])
S(20,[title(20,"채팅이었다면, 처음부터 다시 설명해야 했다"),
  card(20,"quote",0.5,1.7,9,1.1,"\"아이가 6살이고, 많이 못 걷고, 어디서 자고, 원래 일정은…\"",18),
  txt(20,"key",0.5,3.2,9,0.7,"위키는 이미 알고 있다 → 한 문장이면 끝",26,bold=True,color=ACC)])
S(21,[title(21,"쓸수록 이렇게 자란다"),
  txt(21,"sub",0.5,1.2,9,0.5,"실제 6월 도쿄 여행 위키",18,color=MUTED),
  card(21,"n1",0.5,1.9,2.85,2.0,"21\n자료",28,fill=TINT,bold=True,align="CENTER"),
  card(21,"n2",3.575,1.9,2.85,2.0,"31\n페이지",28,fill=TINT,bold=True,align="CENTER"),
  card(21,"n3",6.65,1.9,2.85,2.0,"2\n여행 (도쿄, 제천)",24,fill=TINT,bold=True,align="CENTER"),
  txt(21,"cap",0.5,4.2,9,0.5,"휴대폰 한 화면 요약본까지, 다음 여행은 같은 위키에 쌓인다",18)])
S(22,[title(22,"오늘 정리",0.8),
  txt(22,"pts",0.5,1.4,9,3.3,"LLM 위키는 AI가 쓰고 고치는, 쌓이는 문서\nObsidian, Claude Code, Claudian이면 내 컴퓨터에 만들 수 있다\n사람은 질문과 방향만. 계획이 바뀌어도 한 문장이면 된다",20,bullets=True,space_below=14)])
lead(23,"여러분은 이 위키로\n무엇을 만들고 싶으세요?","여행, 공부, 육아, 취미. 댓글로 알려 주세요","다음 영상: AI 챗봇은 무엇이고, 무엇이 아닌가")
json.dump({"slides":slides},open(sys.argv[1],"w"),ensure_ascii=False,indent=1)
json.dump(bg,open(sys.argv[2],"w"))
