
# NLTK Download Error
```Python
>>> import nltk
>>> nltk.download('stopwords')
[nltk_data] Error loading stopwords: <urlopen error [SSL:
[nltk_data]     CERTIFICATE_VERIFY_FAILED] certificate verify failed:
[nltk_data]     unable to get local issuer certificate (_ssl.c:1091)>
```

## 해결책

http://www.nltk.org/nltk_data/

위 링크로 가서 stopwords zip을 다운받은 후, '/usr/local/share/nltk_data/corpora' 해당 경로에 압축 푼 파일을 넣어주면 된다. 

