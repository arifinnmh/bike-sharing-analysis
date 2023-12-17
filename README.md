# Dicoding Collection Dashboard ✨

## Setup environment
```
conda create --name main-ds python=3.9
conda activate main-ds
pip install numpy pandas scipy matplotlib streamlit
```

## Run steamlit app
```
!wget -q -O - ipv4.icanhazip.com
%%writefile app.py
! streamlit run app.py & npx localtunnel --port 8501
```

