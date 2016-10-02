class mix_chat():
    def __init__(self):
        self.msg_line = {}

    def asking(self, client_name):
        if
    def new_msg(self, text):
        m_list = text.split('::')
        try:
            msg = ''
            if len(m_list) != 0:
                for num, each in enumerate(m_list, start=0):
                    if num != 0:
                        if num ==1:
                            msg += each
                        else:
                            msg += '::' + each
                self.msg_line[m_list[0]] = msg
        except Exception as e:
            print(e)

c = mix_chat()
c.new_msg('yingshaoxo::5201314::6542')
print(c.msg_line)
