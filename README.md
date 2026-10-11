<img src="assets/hero.svg" width="100%" alt="JUNGHOO — Data Engineer · Automation · LLM Tooling" />

### `$ whoami`

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=20&duration=2800&pause=900&color=B13DC8&vCenter=true&width=520&lines=%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%8A%94+%ED%9D%90%EB%A5%B4%EA%B2%8C%2C+%EB%B0%98%EB%B3%B5%EC%9D%80+%EC%BD%94%EB%93%9C%EC%97%90%EA%B2%8C;LLM+%EC%97%90%EC%9D%B4%EC%A0%84%ED%8A%B8%EA%B0%80+%EC%93%B0%EB%8A%94+CLI+%EB%A7%8C%EB%93%A4%EA%B8%B0;UiPath+RPA+%E2%86%92+Python+%EC%9E%90%EB%8F%99%ED%99%94" />

```python
class JungHoo:
    role = "Data Engineer"
    also = "Automation Engineer"  # UiPath RPA → Python

    stack = {
        "data":    ["Airflow", "MySQL", "Hive", "Kafka", "Trino", "ClickHouse"],
        "infra":   ["Docker", "Kubernetes", "CircleCI", "MLflow"],
        "monitor": ["Grafana", "Prometheus"],
        "auto":    ["UiPath", "Slack API", "Flask", "Streamlit", "Puppeteer"],
    }

    def work(self):
        return {
            "pipeline":   "Airflow 로 대규모 배치 설계·운영",
            "recovery":   "체크포인트·재시도로 실패한 단계부터 복구",
            "sdk":        "사내 DB·모니터링·업무 시스템용 Python SDK",
            "automation": "금융·회계·인사 업무 자동화, RPA → Python 전환",
            "ci_cd":      "CircleCI 로 테스트·빌드·배포 자동화, K8s 운영",
        }

    def side(self):
        # 퇴근 후: LLM 에이전트가 셸에서 부르는 조회 CLI
        return ["jibsa", "baenggipyo"]
```

<picture>
  <source media="(prefers-color-scheme: light)" srcset="https://skillicons.dev/icons?i=py%2Cmysql%2Ckafka%2Cdocker%2Ckubernetes%2Cgrafana%2Cprometheus%2Cflask%2Cjs%2Cgit&theme=light" />
  <img src="https://skillicons.dev/icons?i=py,mysql,kafka,docker,kubernetes,grafana,prometheus,flask,js,git&theme=dark" />
</picture>

<br/><br/>

### `$ ls ~/projects`

<a href="https://github.com/Rukkakka/jibsa"><img src="assets/card-jibsa.svg" width="49%" alt="jibsa · 집사" /></a>&nbsp;<a href="https://github.com/Rukkakka/baenggipyo"><img src="assets/card-baenggipyo.svg" width="49%" alt="baenggipyo · 뱅기표" /></a>

<pre>
# jibsa 와 baenggipyo 는 LLM 에이전트가 쓰라고 만든 CLI 입니다
#  - 웹 검색에 걸린 지난 정보 말고, 지금 거래 가능한 것만 가져옵니다
#  - 로그인 없이 볼 수 있는 정보만 쓰고, 사이트별 요청 제한을 지킵니다
#  - 결과는 공통 JSON 으로 돌려주고, 예약·문의는 결과의 url 로 넘깁니다
</pre>

<details open>
<summary><code>$ claude</code> &nbsp;# Claude Code 가 집사로 집을 찾는 모습 (예시 화면)</summary>
<br/>
<img src="assets/jibsa-demo.gif" width="90%" />
</details>

<br/>

### `$ ls ~/libs`

<pre>
<a href="https://github.com/Rukkakka/lib"><b>lib/</b></a>   데이터·모니터링·업무 시스템 클라이언트 래퍼 모음

#  - DB: ClickHouse (동기·비동기), Trino
#  - 모니터링: Grafana, Prometheus
#  - 업무·외부: Slack, Jira, Microsoft Graph, Google Drive·Sheets, 공공데이터포털
#  - 연결 설정은 pydantic 모델로 먼저 검증합니다
#  - 클라이언트는 처음 쓸 때 만들고, with 블록이 끝나면 알아서 닫습니다
#  - HTTP API 는 5xx·429·타임아웃이면 자동으로 다시 시도하고, async 버전도 있습니다
</pre>

<br/>

### `$ git log --stat`

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://streak-stats.demolab.com/?user=Rukkakka&theme=tokyonight&hide_border=true&background=00000000&ring=B13DC8&fire=B13DC8&currStreakLabel=B13DC8" />
  <img src="https://streak-stats.demolab.com/?user=Rukkakka&hide_border=true&background=00000000&ring=7C3AED&fire=B13DC8&currStreakLabel=7C3AED" />
</picture>

### `$ contact`

<pre>
velog   → <a href="https://velog.io/@lcs3947">velog.io/@lcs3947</a>
mail    → <a href="mailto:lcs3947@naver.com">lcs3947@naver.com</a>
</pre>

<img src="https://hits.sh/github.com/Rukkakka.svg?style=flat-square&label=visitors&color=7c3aed" alt="visitors" />
