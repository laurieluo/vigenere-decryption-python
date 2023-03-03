import numpy as np

class FVG:
    '''
    Already known 7:
    
    >>> msg = 'Per zlrracm, vxmcs r qipqlczhs. Qs fcv rihw sxx hblrxh sm nkidhvzphw. Ixxvn qsn, lysh sifecs uui jrrfyg, mk xj suvc kd ss wbrzrrz uqh jpp zyw qv ylgn osfz fin isi bpgyoj, fg dm zdqzap, cl sifecs qks cdfy iu xyxey iu tipp zcni dt. Sin lj nt rfy jszcx hi jik iyfixky iysmh hzuwwwxpk izayv; mw lv olh kfxeu nr gitrhy d afgcr qkiit vjyucsdum bdw kwv cjssiilbcwc kd wwhg e ads, ohg ewuffx fscavuy; lj nt rfy jszcx hi vemt kvy hrmxichpiei rbx giwtrh zxxlgv duqhvbzqm, wlvc ns uui xdzba ws ypms nr hf xk hijikwvf.'
    >>> A = FVG(msg)
    >>> A.get_key(7)
    'PROUDER'
    '''
    def __init__(self, ciphertext):
        self.std_p = [.082,.015,.028,.043,.127,.022,.02,.061,.07,.002,.008,.04,\
                .024,.067,.075,.019,.001,.06,.063,.091,.028,.01,.023,.001,.02,.001]
        self.alpha_list = list(x.upper() for x in ciphertext if x.isalpha())
        self.alpha_n = {chr(x + ord('A')): x for x in range(26)}
        self.n_alpha = {value: key for key, value in self.alpha_n.items()}

    def blocking(self, m):
        block = []
        def helper(slicing):
            if slicing:
                block.append(''.join(slicing[:m]))
                helper(slicing[m:])
        helper(self.alpha_list)
        return block

    def alpha_count(self, m, alpha_num, key_pos, move=0):
        table = self.alpha_list[key_pos::m]
        table = [self.n_alpha[(self.alpha_n[a]-move)%26] for a in table]
        return table.count(self.n_alpha[alpha_num])

    def IC(self, m, key_pos):
        l, helper = len(self.alpha_list) // m, self.alpha_count
        return sum(list((helper(m,x,key_pos)**2-helper(m,x,key_pos)) / (l**2-l) for x in range(26)))

    def IC_(self, m, key_pos):
        def helper(mov):
            l = len(self.alpha_list) // m
            return sum(list(self.alpha_count(m,x,key_pos,mov)*self.std_p[x]/l for x in range(26)))
        return list(helper(mov) for mov in range(26))
        
    def get_key(self, m):
        return ''.join(list(self.n_alpha[self.IC_(m, pos).index(max(self.IC_(m, pos)))] for pos in range(m)))
       


