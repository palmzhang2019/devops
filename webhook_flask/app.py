from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/taiga-webhook', methods=['POST'])
def taiga_webhook():
    # 获取请求的 JSON 数据
    data = request.json
    print(data)
    # 在此处处理接收到的 Webhook 数据
    # 例如，您可以根据数据在 Forgejo 中创建相应的 Issue

    # 返回响应
    return jsonify({'message': 'Webhook received successfully!'}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
