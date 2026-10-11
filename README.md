<img src="assets/hero.svg" width="100%" alt="JUNGHOO — Data Engineer · Automation · LLM Tooling" />

### `$ whoami`

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=20&duration=2800&pause=900&color=B13DC8&vCenter=true&width=520&lines=%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%8A%94+%ED%9D%90%EB%A5%B4%EA%B2%8C%2C+%EB%B0%98%EB%B3%B5%EC%9D%80+%EC%BD%94%EB%93%9C%EC%97%90%EA%B2%8C;LLM+%EC%97%90%EC%9D%B4%EC%A0%84%ED%8A%B8%EA%B0%80+%EC%93%B0%EB%8A%94+CLI+%EB%A7%8C%EB%93%A4%EA%B8%B0;UiPath+RPA+%E2%86%92+Python+%EC%9E%90%EB%8F%99%ED%99%94" />

```python
class JungHoo:
    role = "Data Engineer"
    also = "Automation Engineer"  # UiPath RPA → Python

    stack = {
        "data":  ["MySQL", "Hive", "Kafka", "Trino", "ClickHouse", "MLflow"],
        "infra": ["Docker", "Kubernetes", "Grafana", "Prometheus"],
        "auto":  ["UiPath", "Slack API", "Flask", "Streamlit", "Puppeteer"],
    }

    def pipeline(self):
        # 천만 건 단위 배치. 운영 DB 는 chunk 로 나눠 읽고,
        # 단계마다 parquet 체크포인트를 남겨 실패한 단계부터 다시 돈다
        return (
            extract(mysql, hive)
            >> preprocess
            >> predict(mlflow)
            >> load(kafka)
        )

    def now(self):
        # LLM 에이전트가 셸에서 직접 부르는 조회 CLI
        return ["jibsa", "baenggipyo"]
```

<picture>
  <source media="(prefers-color-scheme: light)" srcset="https://skillicons.dev/icons?i=py,mysql,kafka,docker,kubernetes,grafana,prometheus,flask,js,git&theme=light" />
  <img src="https://skillicons.dev/icons?i=py,mysql,kafka,docker,kubernetes,grafana,prometheus,flask,js,git&theme=dark" />
</picture>

<br/><br/>

### `$ ls ~/projects`

<a href="https://github.com/Rukkakka/jibsa"><img src="assets/card-jibsa.svg" width="49%" alt="jibsa · 집사" /></a>&nbsp;<a href="https://github.com/Rukkakka/baenggipyo"><img src="assets/card-baenggipyo.svg" width="49%" alt="baenggipyo · 뱅기표" /></a>

<pre>
<a href="https://github.com/Rukkakka/lib"><b>lib/</b></a>   ClickHouse·Trino·Grafana·Slack 클라이언트 래퍼

# jibsa 와 baenggipyo 는 LLM 에이전트가 쓰라고 만든 형제 CLI 입니다
#  - 웹 검색에 걸린 지난 정보 말고, 지금 거래 가능한 것만 가져옵니다
#  - 로그인 없이 볼 수 있는 정보만 쓰고, 사이트별 요청 제한을 지킵니다
#  - 결과는 공통 JSON 으로 돌려주고, 예약·문의는 결과의 url 로 넘깁니다
</pre>

<details open>
<summary><code>$ jibsa</code> &nbsp;# 직방·네이버·당근을 조건 바꿔 가며 조회 (예시 데이터)</summary>
<br/>
<img src="assets/jibsa-demo.gif" width="90%" />
</details>

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

<img src="https://komarev.com/ghpvc/?username=Rukkakka&color=7C3AED&style=flat-square&label=visitors" />
