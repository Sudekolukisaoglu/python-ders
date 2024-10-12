print("Chat GPTV'ye hoş geldin.")

cevap = input("Nasılsın.")
#if cevap == 'iyiym' or cevap =='iyi' or cevap =='güzel':
if cevap in ['iyiyim','iyi','güzel']: #bu ve üst satır aynı işi yapar
  print("Güzel. İyi olmana sevindim.")

if cevap in ['kötü', 'moralim bozuk']:
    c = input('hayırdır ne oldu?')
    if c in ['Sınavım kötü geçti','sınav kötüydü','istediğim motor satılomış'.]:
        print ('Böyle şeyleri takma.')
    elif c in ['Otobüsü kaçırdım.','sınav kötüydü']:
        print ('sonraki sefere, olmaz inş.')    
input()
