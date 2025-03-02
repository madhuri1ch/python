def lengthOfLongestSubstring( s: str) -> int:
      glong=""
      glen=0
      sub=""
      n=len(s)
      for i in range(n):
        print('s of i')
        print(s[i])
        if s[i] in sub:
          print('yes{} in sub {}'.format(s[i],sub))
          lenofsub=len(sub)
          if glen<(lenofsub):
            glong=sub
            glen=len(glong)
          sub=sub[sub.index(s[i])+1:]+s[i]
          print('sub after slice:{}'.format(sub))
          
        else:
          sub+=s[i]
          print('in else for {},sub={}'.format(s[i],sub))
      if glen<(len(sub)):
            glong=sub
            glen=len(glong)  
      print(glong)
      return len(glong)
        
print(lengthOfLongestSubstring('abcabcbb'))