# 使用官方的 Python 基础镜像
FROM python:3.8.20

# 设置工作目录（无需复制代码）
WORKDIR /app

# 安装所需的 Python 包
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# 暴露 Flask 应用程序的端口
EXPOSE 5000

# 运行 Flask 应用程序
CMD ["python", "app.py"]
