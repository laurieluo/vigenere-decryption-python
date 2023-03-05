# vigenere-decryption-python
decrypt ciphertext of vigenere to plaintext with python

## doctest:

`$ python3 -m doctest -v FVG.py`

## usage:

```python
>>> msg = 'Per zlrracm, vxmcs r qipqlczhs. Qs fcv rihw sxx hblrxh sm nkidhvzphw. Ixxvn qsn, lysh sifecs uui jrrfyg, mk xj suvc kd ss wbrzrrz uq      h jpp zyw qv ylgn osfz fin isi bpgyoj, fg dm zdqzap, cl sifecs qks cdfy iu xyxey iu tipp zcni dt. Sin lj nt rfy jszcx hi jik iyfixky iysmh hzuwwwxp      k izayv; mw lv olh kfxeu nr gitrhy d afgcr qkiit vjyucsdum bdw kwv cjssiilbcwc kd wwhg e ads, ohg ewuffx fscavuy; lj nt rfy jszcx hi vemt kvy hrmxi      chpiei rbx giwtrh zxxlgv duqhvbzqm, wlvc ns uui xdzba ws ypms nr hf xk hijikwvf.'
>>> a = FVG(msg)
>>> a.suggested_key_len
7
>>> a.get_key(a.suggested_key_len)
'PROUDER'
```
