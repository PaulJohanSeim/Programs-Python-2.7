# Copyright Paul-Johan Seim

s='ghfoghoeghoegoegho'
longest = 0
# print s
maxindex = len(s) - 1 # index of string of length n is (n-1)
lastword = s[0];
for count in range(len(s)):
  temp = 1
  tempcount = count
  tempword = s[count]
  nextcount = tempcount + 1
  while tempcount < maxindex:
    done = 0
    # print "done ", done
    while (done < 1):
      # print "nextcount ", nextcount," tempcount ", tempcount
      if nextcount > maxindex:
        done = 1
      else:
        templetter = s[tempcount]
        nextletter = s[nextcount]
        # print "templetter ", templetter, " nextletter ", nextletter
        tempvalue = ord(templetter)
        nextvalue = ord(nextletter)
        # print "tempvalue ", tempvalue, " nextletter ", nextvalue
        if nextvalue >= tempvalue:
          temp += 1
          tempword += nextletter
          # print "tempword ", tempword
          # print "lastword ", lastword
          if len(tempword) > len(lastword):
            longest = temp
            lastword = tempword
        else:
          done = 1
          temp = 1
          tempword = ""
      tempcount += 1
      nextcount = tempcount + 1
    # print "tempcount ", tempcount, ", temp ", temp
    # print "Longest substring in alphabetical order length is:", longest
print "Longest substring in alphabetical order is: ", lastword
