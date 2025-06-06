
```index.html
<!DOCTYPE html>
<html lang="ja">

<head>
    <meta charset="UTF-8">
    <title>チャット形式メモアプリ</title>
    <!-- QRCodeライブラリを先に読み込む -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/qrcodejs/1.0.0/qrcode.min.js"></script>
    <style>
        body {
            width: 300px;
            font-family: Arial, sans-serif;
        }

        #chat-container {
            height: 300px;
            overflow-y: auto;
            border: 1px solid #ccc;
            padding: 10px;
        }

        .message {
            margin-bottom: 10px;
        }

        .message .actions {
            font-size: 0.8em;
            color: #888;
        }

        #input-container {
            margin-top: 10px;
        }

        #message-input {
            width: 70%;
        }

        /* QRコード用の新しいスタイル */
        .qr-codes {
            margin: 10px 0;
        }

        .qr-wrapper {
            margin: 10px 0;
            padding: 10px;
            background: #f5f5f5;
            border-radius: 4px;
        }

        .url-text {
            margin-bottom: 5px;
            word-break: break-all;
            font-size: 0.9em;
            color: #0066cc;
        }

        .qr-code {
            display: inline-block;
        }

        .qr-code img {
            display: block;
            margin: 0 auto;
        }
    </style>
</head>

<body>
    <div id="chat-container"></div>
    <div id="input-container">
        <input type="text" id="message-input" placeholder="メッセージを入力">
        <button id="send-button">送信</button>
    </div>
    <!-- script.jsを後で読み込む -->
    <script src="script.js"></script>
</body>

</html>
```

```script.js
document.addEventListener('DOMContentLoaded', () => {
    const chatContainer = document.getElementById('chat-container');
    const messageInput = document.getElementById('message-input');
    const sendButton = document.getElementById('send-button');

    let messages = [];

    // メッセージを読み込む
    chrome.storage.local.get(['messages'], (result) => {
        if (result.messages) {
            messages = result.messages;
            renderMessages();
        }
    });

    // メッセージを保存する関数
    function saveMessages() {
        chrome.storage.local.set({ messages: messages }, () => {
            console.log('メッセージが保存されました');
        });
    }

    // メッセージを表示する関数
    function renderMessages() {
        chatContainer.innerHTML = '';
        messages.forEach((msg, index) => {
            const messageElement = document.createElement('div');
            messageElement.className = 'message';

            // メッセージテキストの div
            const textDiv = document.createElement('div');
            textDiv.textContent = msg.text;

            // URL を検出して QR コードを生成
            const urls = extractUrls(msg.text);
            const qrContainer = document.createElement('div');
            qrContainer.className = 'qr-codes';

            if (urls.length > 0) {
                urls.forEach(url => {
                    const qrWrapper = document.createElement('div');
                    qrWrapper.className = 'qr-wrapper';

                    // URL 表示
                    const urlText = document.createElement('div');
                    urlText.className = 'url-text';
                    urlText.textContent = url;
                    qrWrapper.appendChild(urlText);

                    // QR コード生成用の div
                    const qrElement = document.createElement('div');
                    qrElement.className = 'qr-code';
                    qrWrapper.appendChild(qrElement);

                    // QR コード生成
                    new QRCode(qrElement, {
                        text: url,
                        width: 128,
                        height: 128,
                        colorDark: "#000000",
                        colorLight: "#ffffff",
                        correctLevel: QRCode.CorrectLevel.H
                    });

                    qrContainer.appendChild(qrWrapper);
                });
            }

            // アクション部分
            const actionsDiv = document.createElement('div');
            actionsDiv.className = 'actions';
            actionsDiv.innerHTML = `
            <a href="#" class="edit" data-id="${index}">編集</a> | 
            <a href="#" class="delete" data-id="${index}">削除</a>
        `;

            messageElement.appendChild(textDiv);
            messageElement.appendChild(qrContainer);
            messageElement.appendChild(actionsDiv);

            chatContainer.appendChild(messageElement);
        });
        chatContainer.scrollTop = chatContainer.scrollHeight;
    }

    // URL 抽出用の新しい関数を追加
    function extractUrls(text) {
        const urlRegex = /(https?:\/\/[^\s]+)/g;
        return text.match(urlRegex) || [];
    }

    // メッセージを追加する関数
    function addMessage(text) {
        messages.push({ text: text, timestamp: new Date().getTime() });
        saveMessages();
        renderMessages();
    }

    // 送信ボタンのクリックイベント
    sendButton.addEventListener('click', () => {
        const text = messageInput.value.trim();
        if (text) {
            addMessage(text);
            messageInput.value = '';
        }
    });

    // Enterキーでの送信
    messageInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            sendButton.click();
        }
    });

    // 編集と削除の機能
    chatContainer.addEventListener('click', (e) => {
        if (e.target.classList.contains('edit')) {
            const id = e.target.getAttribute('data-id');
            const newText = prompt('メッセージを編集', messages[id].text);
            if (newText !== null) {
                messages[id].text = newText;
                saveMessages();
                renderMessages();
            }
        } else if (e.target.classList.contains('delete')) {
            const id = e.target.getAttribute('data-id');
            if (confirm('このメッセージを削除しますか？')) {
                messages.splice(id, 1);
                saveMessages();
                renderMessages();
            }
        }
    });
});
```

```manifest.json
{
    "manifest_version": 2,
    "name": "メモアプリ",
    "version": "1.0",
    "description": "Zoomやライブ配信用のメモアプリ",
    "permissions": [
        "storage"
    ],
    "content_security_policy": "script-src 'self' https://cdnjs.cloudflare.com; object-src 'self'",
    "browser_action": {
        "default_popup": "index.html"
    }
}
```
