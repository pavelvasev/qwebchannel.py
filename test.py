if __name__ == '__main__':
    from qwebchannel import QWebchannel
    import websocket

    def on_message(ws, message):
        print(message)

    def on_error(ws, error):
        print(error)

    def on_close(ws):
        print("### closed ###")

    def channel_ready(channel):
        objApp = channel.objects.WizExplorerApp
        objApp.Window.CurrentDocument(lambda doc: print(doc.Title))

    def on_open(ws):
        QWebchannel(ws, channel_ready)

    if __name__ == "__main__":
        websocket.enableTrace(False)
        ws = websocket.WebSocketApp("ws://127.0.0.1:8848",
                                    on_message=on_message,
                                    on_error=on_error,
                                    on_close=on_close)
        ws.on_open = on_open
        ws.run_forever()