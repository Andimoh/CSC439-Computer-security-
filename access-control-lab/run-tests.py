#! python3

import subprocess

total= 0
args= ['sudo','-u','bard','./check-perm','Jones-Pleading1.txt','R','T','bard']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','bard','./check-perm','Jones-Pleading1.txt','W','T','bard']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','sam','./check-perm','Jones-Pleading1.txt','R','T','sam']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','sam','./check-perm','Jones-Pleading1.txt','W','T','sam']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','mary','./check-perm','Jones-Pleading1.txt','R','T','mary']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','mary','./check-perm','Jones-Pleading1.txt','W','T','mary']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','bob','./check-perm','Jones-Pleading1.txt','R','T','bob']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','bob','./check-perm','Jones-Pleading1.txt','W','T','bob']
total+= subprocess.run( args ).returncode

args= ['sudo','-u','karen','./check-perm','Jones-Pleading1.txt','R','T','karen']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','karen','./check-perm','Jones-Pleading1.txt','W','F','karen']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','kevin','./check-perm','Jones-Pleading1.txt','R','T','kevin']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','kevin','./check-perm','Jones-Pleading1.txt','W','F','kevin']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','tom','./check-perm','Jones-Pleading1.txt','R','T','tom']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','tom','./check-perm','Jones-Pleading1.txt','W','F','tom']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','becky','./check-perm','Jones-Pleading1.txt','R','T','becky']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','becky','./check-perm','Jones-Pleading1.txt','W','F','becky']
total+= subprocess.run( args ).returncode

args= ['sudo','-u','bard','./check-perm','Jones-Pleading2.txt','R','T','bard']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','bard','./check-perm','Jones-Pleading2.txt','W','T','bard']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','sam','./check-perm','Jones-Pleading2.txt','R','T','sam']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','sam','./check-perm','Jones-Pleading2.txt','W','T','sam']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','mary','./check-perm','Jones-Pleading2.txt','R','T','mary']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','mary','./check-perm','Jones-Pleading2.txt','W','T','mary']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','bob','./check-perm','Jones-Pleading2.txt','R','T','bob']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','bob','./check-perm','Jones-Pleading2.txt','W','T','bob']
total+= subprocess.run( args ).returncode

args= ['sudo','-u','karen','./check-perm','Jones-Pleading2.txt','R','T','karen']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','karen','./check-perm','Jones-Pleading2.txt','W','F','karen']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','kevin','./check-perm','Jones-Pleading2.txt','R','T','kevin']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','kevin','./check-perm','Jones-Pleading2.txt','W','F','kevin']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','tom','./check-perm','Jones-Pleading2.txt','R','T','tom']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','tom','./check-perm','Jones-Pleading2.txt','W','F','tom']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','becky','./check-perm','Jones-Pleading2.txt','R','T','becky']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','becky','./check-perm','Jones-Pleading2.txt','W','F','becky']
total+= subprocess.run( args ).returncode

args= ['sudo','-u','bard','./check-perm','Johnson-Contract1.txt','R','T','bard']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','bard','./check-perm','Johnson-Contract1.txt','W','F','bard']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','sam','./check-perm','Johnson-Contract1.txt','R','T','sam']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','sam','./check-perm','Johnson-Contract1.txt','W','F','sam']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','mary','./check-perm','Johnson-Contract1.txt','R','T','mary']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','mary','./check-perm','Johnson-Contract1.txt','W','F','mary']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','bob','./check-perm','Johnson-Contract1.txt','R','T','bob']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','bob','./check-perm','Johnson-Contract1.txt','W','F','bob']
total+= subprocess.run( args ).returncode

args= ['sudo','-u','karen','./check-perm','Johnson-Contract1.txt','R','T','karen']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','karen','./check-perm','Johnson-Contract1.txt','W','T','karen']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','kevin','./check-perm','Johnson-Contract1.txt','R','T','kevin']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','kevin','./check-perm','Johnson-Contract1.txt','W','T','kevin']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','tom','./check-perm','Johnson-Contract1.txt','R','T','tom']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','tom','./check-perm','Johnson-Contract1.txt','W','T','tom']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','becky','./check-perm','Johnson-Contract1.txt','R','T','becky']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','becky','./check-perm','Johnson-Contract1.txt','W','T','becky']
total+= subprocess.run( args ).returncode

args= ['sudo','-u','bard','./check-perm','Johnson-Contract2.txt','R','T','bard']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','bard','./check-perm','Johnson-Contract2.txt','W','F','bard']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','sam','./check-perm','Johnson-Contract2.txt','R','T','sam']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','sam','./check-perm','Johnson-Contract2.txt','W','F','sam']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','mary','./check-perm','Johnson-Contract2.txt','R','T','mary']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','mary','./check-perm','Johnson-Contract2.txt','W','F','mary']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','bob','./check-perm','Johnson-Contract2.txt','R','T','bob']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','bob','./check-perm','Johnson-Contract2.txt','W','F','bob']
total+= subprocess.run( args ).returncode

args= ['sudo','-u','karen','./check-perm','Johnson-Contract2.txt','R','T','karen']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','karen','./check-perm','Johnson-Contract2.txt','W','T','karen']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','kevin','./check-perm','Johnson-Contract2.txt','R','T','kevin']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','kevin','./check-perm','Johnson-Contract2.txt','W','T','kevin']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','tom','./check-perm','Johnson-Contract2.txt','R','T','tom']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','tom','./check-perm','Johnson-Contract2.txt','W','T','tom']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','becky','./check-perm','Johnson-Contract2.txt','R','T','becky']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','becky','./check-perm','Johnson-Contract2.txt','W','T','becky']
total+= subprocess.run( args ).returncode

args= ['sudo','-u','bard','./check-perm','Santana-Pleading1.txt','R','T','bard']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','bard','./check-perm','Santana-Pleading1.txt','W','T','bard']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','sam','./check-perm','Santana-Pleading1.txt','R','T','sam']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','sam','./check-perm','Santana-Pleading1.txt','W','T','sam']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','mary','./check-perm','Santana-Pleading1.txt','R','T','mary']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','mary','./check-perm','Santana-Pleading1.txt','W','T','mary']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','bob','./check-perm','Santana-Pleading1.txt','R','T','bob']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','bob','./check-perm','Santana-Pleading1.txt','W','T','bob']
total+= subprocess.run( args ).returncode

args= ['sudo','-u','karen','./check-perm','Santana-Pleading1.txt','R','T','karen']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','karen','./check-perm','Santana-Pleading1.txt','W','F','karen']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','kevin','./check-perm','Santana-Pleading1.txt','R','T','kevin']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','kevin','./check-perm','Santana-Pleading1.txt','W','F','kevin']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','tom','./check-perm','Santana-Pleading1.txt','R','T','tom']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','tom','./check-perm','Santana-Pleading1.txt','W','F','tom']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','becky','./check-perm','Santana-Pleading1.txt','R','T','becky']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','becky','./check-perm','Santana-Pleading1.txt','W','F','becky']
total+= subprocess.run( args ).returncode

args= ['sudo','-u','bard','./check-perm','Santana-Pleading2.txt','R','T','bard']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','bard','./check-perm','Santana-Pleading2.txt','W','T','bard']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','sam','./check-perm','Santana-Pleading2.txt','R','T','sam']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','sam','./check-perm','Santana-Pleading2.txt','W','T','sam']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','mary','./check-perm','Santana-Pleading2.txt','R','T','mary']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','mary','./check-perm','Santana-Pleading2.txt','W','T','mary']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','bob','./check-perm','Santana-Pleading2.txt','R','T','bob']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','bob','./check-perm','Santana-Pleading2.txt','W','T','bob']
total+= subprocess.run( args ).returncode

args= ['sudo','-u','karen','./check-perm','Santana-Pleading2.txt','R','T','karen']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','karen','./check-perm','Santana-Pleading2.txt','W','F','karen']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','kevin','./check-perm','Santana-Pleading2.txt','R','T','kevin']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','kevin','./check-perm','Santana-Pleading2.txt','W','F','kevin']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','tom','./check-perm','Santana-Pleading2.txt','R','T','tom']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','tom','./check-perm','Santana-Pleading2.txt','W','F','tom']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','becky','./check-perm','Santana-Pleading2.txt','R','T','becky']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','becky','./check-perm','Santana-Pleading2.txt','W','F','becky']
total+= subprocess.run( args ).returncode

args= ['sudo','-u','bard','./check-perm','Jones-Bill1.txt','R','T','bard']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','bard','./check-perm','Jones-Bill1.txt','W','T','bard']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','sam','./check-perm','Jones-Bill1.txt','R','T','sam']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','sam','./check-perm','Jones-Bill1.txt','W','T','sam']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','mary','./check-perm','Jones-Bill1.txt','R','T','mary']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','mary','./check-perm','Jones-Bill1.txt','W','T','mary']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','bob','./check-perm','Jones-Bill1.txt','R','T','bob']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','bob','./check-perm','Jones-Bill1.txt','W','T','bob']
total+= subprocess.run( args ).returncode

args= ['sudo','-u','karen','./check-perm','Jones-Bill1.txt','R','T','karen']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','karen','./check-perm','Jones-Bill1.txt','W','T','karen']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','kevin','./check-perm','Jones-Bill1.txt','R','T','kevin']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','kevin','./check-perm','Jones-Bill1.txt','W','T','kevin']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','tom','./check-perm','Jones-Bill1.txt','R','F','tom']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','tom','./check-perm','Jones-Bill1.txt','W','F','tom']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','becky','./check-perm','Jones-Bill1.txt','R','F','becky']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','becky','./check-perm','Jones-Bill1.txt','W','F','becky']
total+= subprocess.run( args ).returncode

args= ['sudo','-u','bard','./check-perm','Jones-Bill2.txt','R','T','bard']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','bard','./check-perm','Jones-Bill2.txt','W','T','bard']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','sam','./check-perm','Jones-Bill2.txt','R','T','sam']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','sam','./check-perm','Jones-Bill2.txt','W','T','sam']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','mary','./check-perm','Jones-Bill2.txt','R','T','mary']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','mary','./check-perm','Jones-Bill2.txt','W','T','mary']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','bob','./check-perm','Jones-Bill2.txt','R','T','bob']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','bob','./check-perm','Jones-Bill2.txt','W','T','bob']
total+= subprocess.run( args ).returncode

args= ['sudo','-u','karen','./check-perm','Jones-Bill2.txt','R','T','karen']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','karen','./check-perm','Jones-Bill2.txt','W','T','karen']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','kevin','./check-perm','Jones-Bill2.txt','R','T','kevin']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','kevin','./check-perm','Jones-Bill2.txt','W','T','kevin']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','tom','./check-perm','Jones-Bill2.txt','R','F','tom']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','tom','./check-perm','Jones-Bill2.txt','W','F','tom']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','becky','./check-perm','Jones-Bill2.txt','R','F','becky']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','becky','./check-perm','Jones-Bill2.txt','W','F','becky']
total+= subprocess.run( args ).returncode

args= ['sudo','-u','bard','./check-perm','Santana-Bill1.txt','R','T','bard']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','bard','./check-perm','Santana-Bill1.txt','W','T','bard']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','sam','./check-perm','Santana-Bill1.txt','R','T','sam']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','sam','./check-perm','Santana-Bill1.txt','W','T','sam']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','mary','./check-perm','Santana-Bill1.txt','R','T','mary']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','mary','./check-perm','Santana-Bill1.txt','W','T','mary']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','bob','./check-perm','Santana-Bill1.txt','R','T','bob']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','bob','./check-perm','Santana-Bill1.txt','W','T','bob']
total+= subprocess.run( args ).returncode

args= ['sudo','-u','karen','./check-perm','Santana-Bill1.txt','R','T','karen']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','karen','./check-perm','Santana-Bill1.txt','W','T','karen']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','kevin','./check-perm','Santana-Bill1.txt','R','T','kevin']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','kevin','./check-perm','Santana-Bill1.txt','W','T','kevin']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','tom','./check-perm','Santana-Bill1.txt','R','F','tom']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','tom','./check-perm','Santana-Bill1.txt','W','F','tom']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','becky','./check-perm','Santana-Bill1.txt','R','F','becky']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','becky','./check-perm','Santana-Bill1.txt','W','F','becky']
total+= subprocess.run( args ).returncode

args= ['sudo','-u','bard','./check-perm','Santana-Bill2.txt','R','T','bard']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','bard','./check-perm','Santana-Bill2.txt','W','T','bard']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','sam','./check-perm','Santana-Bill2.txt','R','T','sam']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','sam','./check-perm','Santana-Bill2.txt','W','T','sam']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','mary','./check-perm','Santana-Bill2.txt','R','T','mary']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','mary','./check-perm','Santana-Bill2.txt','W','T','mary']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','bob','./check-perm','Santana-Bill2.txt','R','T','bob']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','bob','./check-perm','Santana-Bill2.txt','W','T','bob']
total+= subprocess.run( args ).returncode

args= ['sudo','-u','karen','./check-perm','Santana-Bill2.txt','R','T','karen']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','karen','./check-perm','Santana-Bill2.txt','W','T','karen']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','kevin','./check-perm','Santana-Bill2.txt','R','T','kevin']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','kevin','./check-perm','Santana-Bill2.txt','W','T','kevin']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','tom','./check-perm','Santana-Bill2.txt','R','F','tom']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','tom','./check-perm','Santana-Bill2.txt','W','F','tom']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','becky','./check-perm','Santana-Bill2.txt','R','F','becky']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','becky','./check-perm','Santana-Bill2.txt','W','F','becky']
total+= subprocess.run( args ).returncode

args= ['sudo','-u','bard','./check-perm','Johnson-Bill1.txt','R','T','bard']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','bard','./check-perm','Johnson-Bill1.txt','W','T','bard']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','sam','./check-perm','Johnson-Bill1.txt','R','T','sam']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','sam','./check-perm','Johnson-Bill1.txt','W','T','sam']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','mary','./check-perm','Johnson-Bill1.txt','R','F','mary']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','mary','./check-perm','Johnson-Bill1.txt','W','F','mary']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','bob','./check-perm','Johnson-Bill1.txt','R','F','bob']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','bob','./check-perm','Johnson-Bill1.txt','W','F','bob']
total+= subprocess.run( args ).returncode

args= ['sudo','-u','karen','./check-perm','Johnson-Bill1.txt','R','T','karen']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','karen','./check-perm','Johnson-Bill1.txt','W','T','karen']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','kevin','./check-perm','Johnson-Bill1.txt','R','T','kevin']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','kevin','./check-perm','Johnson-Bill1.txt','W','T','kevin']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','tom','./check-perm','Johnson-Bill1.txt','R','T','tom']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','tom','./check-perm','Johnson-Bill1.txt','W','T','tom']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','becky','./check-perm','Johnson-Bill1.txt','R','T','becky']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','becky','./check-perm','Johnson-Bill1.txt','W','T','becky']
total+= subprocess.run( args ).returncode

args= ['sudo','-u','bard','./check-perm','Johnson-Bill2.txt','R','T','bard']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','bard','./check-perm','Johnson-Bill2.txt','W','T','bard']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','sam','./check-perm','Johnson-Bill2.txt','R','T','sam']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','sam','./check-perm','Johnson-Bill2.txt','W','T','sam']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','mary','./check-perm','Johnson-Bill2.txt','R','F','mary']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','mary','./check-perm','Johnson-Bill2.txt','W','F','mary']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','bob','./check-perm','Johnson-Bill2.txt','R','F','bob']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','bob','./check-perm','Johnson-Bill2.txt','W','F','bob']
total+= subprocess.run( args ).returncode

args= ['sudo','-u','karen','./check-perm','Johnson-Bill2.txt','R','T','karen']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','karen','./check-perm','Johnson-Bill2.txt','W','T','karen']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','kevin','./check-perm','Johnson-Bill2.txt','R','T','kevin']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','kevin','./check-perm','Johnson-Bill2.txt','W','T','kevin']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','tom','./check-perm','Johnson-Bill2.txt','R','T','tom']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','tom','./check-perm','Johnson-Bill2.txt','W','T','tom']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','becky','./check-perm','Johnson-Bill2.txt','R','T','becky']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','becky','./check-perm','Johnson-Bill2.txt','W','T','becky']
total+= subprocess.run( args ).returncode

args= ['sudo','-u','bard','./check-perm','Jones-Court1.txt','R','T','bard']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','bard','./check-perm','Jones-Court1.txt','W','T','bard']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','sam','./check-perm','Jones-Court1.txt','R','T','sam']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','sam','./check-perm','Jones-Court1.txt','W','F','sam']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','mary','./check-perm','Jones-Court1.txt','R','T','mary']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','mary','./check-perm','Jones-Court1.txt','W','F','mary']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','bob','./check-perm','Jones-Court1.txt','R','T','bob']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','bob','./check-perm','Jones-Court1.txt','W','F','bob']
total+= subprocess.run( args ).returncode

args= ['sudo','-u','karen','./check-perm','Jones-Court1.txt','R','T','karen']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','karen','./check-perm','Jones-Court1.txt','W','F','karen']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','kevin','./check-perm','Jones-Court1.txt','R','T','kevin']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','kevin','./check-perm','Jones-Court1.txt','W','F','kevin']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','tom','./check-perm','Jones-Court1.txt','R','T','tom']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','tom','./check-perm','Jones-Court1.txt','W','F','tom']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','becky','./check-perm','Jones-Court1.txt','R','T','becky']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','becky','./check-perm','Jones-Court1.txt','W','F','becky']
total+= subprocess.run( args ).returncode

args= ['sudo','-u','bard','./check-perm','Jones-Court2.txt','R','T','bard']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','bard','./check-perm','Jones-Court2.txt','W','F','bard']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','sam','./check-perm','Jones-Court2.txt','R','T','sam']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','sam','./check-perm','Jones-Court2.txt','W','F','sam']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','mary','./check-perm','Jones-Court2.txt','R','T','mary']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','mary','./check-perm','Jones-Court2.txt','W','T','mary']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','bob','./check-perm','Jones-Court2.txt','R','T','bob']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','bob','./check-perm','Jones-Court2.txt','W','F','bob']
total+= subprocess.run( args ).returncode

args= ['sudo','-u','karen','./check-perm','Jones-Court2.txt','R','T','karen']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','karen','./check-perm','Jones-Court2.txt','W','F','karen']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','kevin','./check-perm','Jones-Court2.txt','R','T','kevin']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','kevin','./check-perm','Jones-Court2.txt','W','F','kevin']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','tom','./check-perm','Jones-Court2.txt','R','T','tom']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','tom','./check-perm','Jones-Court2.txt','W','F','tom']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','becky','./check-perm','Jones-Court2.txt','R','T','becky']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','becky','./check-perm','Jones-Court2.txt','W','F','becky']
total+= subprocess.run( args ).returncode

args= ['sudo','-u','bard','./check-perm','Santana-Court1.txt','R','T','bard']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','bard','./check-perm','Santana-Court1.txt','W','F','bard']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','sam','./check-perm','Santana-Court1.txt','R','T','sam']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','sam','./check-perm','Santana-Court1.txt','W','F','sam']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','mary','./check-perm','Santana-Court1.txt','R','T','mary']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','mary','./check-perm','Santana-Court1.txt','W','F','mary']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','bob','./check-perm','Santana-Court1.txt','R','T','bob']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','bob','./check-perm','Santana-Court1.txt','W','T','bob']
total+= subprocess.run( args ).returncode

args= ['sudo','-u','karen','./check-perm','Santana-Court1.txt','R','T','karen']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','karen','./check-perm','Santana-Court1.txt','W','F','karen']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','kevin','./check-perm','Santana-Court1.txt','R','T','kevin']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','kevin','./check-perm','Santana-Court1.txt','W','F','kevin']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','tom','./check-perm','Santana-Court1.txt','R','T','tom']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','tom','./check-perm','Santana-Court1.txt','W','F','tom']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','becky','./check-perm','Santana-Court1.txt','R','T','becky']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','becky','./check-perm','Santana-Court1.txt','W','F','becky']
total+= subprocess.run( args ).returncode

args= ['sudo','-u','bard','./check-perm','Santana-Court2.txt','R','T','bard']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','bard','./check-perm','Santana-Court2.txt','W','F','bard']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','sam','./check-perm','Santana-Court2.txt','R','T','sam']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','sam','./check-perm','Santana-Court2.txt','W','F','sam']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','mary','./check-perm','Santana-Court2.txt','R','T','mary']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','mary','./check-perm','Santana-Court2.txt','W','F','mary']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','bob','./check-perm','Santana-Court2.txt','R','T','bob']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','bob','./check-perm','Santana-Court2.txt','W','T','bob']
total+= subprocess.run( args ).returncode

args= ['sudo','-u','karen','./check-perm','Santana-Court2.txt','R','T','karen']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','karen','./check-perm','Santana-Court2.txt','W','F','karen']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','kevin','./check-perm','Santana-Court2.txt','R','T','kevin']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','kevin','./check-perm','Santana-Court2.txt','W','F','kevin']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','tom','./check-perm','Santana-Court2.txt','R','T','tom']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','tom','./check-perm','Santana-Court2.txt','W','F','tom']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','becky','./check-perm','Santana-Court2.txt','R','T','becky']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','becky','./check-perm','Santana-Court2.txt','W','F','becky']
total+= subprocess.run( args ).returncode

args= ['sudo','-u','bard','./check-perm','Johnson-Meeting1.txt','R','T','bard']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','bard','./check-perm','Johnson-Meeting1.txt','W','F','bard']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','sam','./check-perm','Johnson-Meeting1.txt','R','T','sam']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','sam','./check-perm','Johnson-Meeting1.txt','W','F','sam']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','mary','./check-perm','Johnson-Meeting1.txt','R','T','mary']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','mary','./check-perm','Johnson-Meeting1.txt','W','F','mary']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','bob','./check-perm','Johnson-Meeting1.txt','R','T','bob']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','bob','./check-perm','Johnson-Meeting1.txt','W','F','bob']
total+= subprocess.run( args ).returncode

args= ['sudo','-u','karen','./check-perm','Johnson-Meeting1.txt','R','T','karen']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','karen','./check-perm','Johnson-Meeting1.txt','W','T','karen']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','kevin','./check-perm','Johnson-Meeting1.txt','R','T','kevin']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','kevin','./check-perm','Johnson-Meeting1.txt','W','F','kevin']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','tom','./check-perm','Johnson-Meeting1.txt','R','T','tom']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','tom','./check-perm','Johnson-Meeting1.txt','W','F','tom']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','becky','./check-perm','Johnson-Meeting1.txt','R','T','becky']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','becky','./check-perm','Johnson-Meeting1.txt','W','F','becky']
total+= subprocess.run( args ).returncode

args= ['sudo','-u','bard','./check-perm','Johnson-Meeting2.txt','R','T','bard']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','bard','./check-perm','Johnson-Meeting2.txt','W','F','bard']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','sam','./check-perm','Johnson-Meeting2.txt','R','T','sam']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','sam','./check-perm','Johnson-Meeting2.txt','W','F','sam']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','mary','./check-perm','Johnson-Meeting2.txt','R','T','mary']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','mary','./check-perm','Johnson-Meeting2.txt','W','F','mary']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','bob','./check-perm','Johnson-Meeting2.txt','R','T','bob']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','bob','./check-perm','Johnson-Meeting2.txt','W','F','bob']
total+= subprocess.run( args ).returncode

args= ['sudo','-u','karen','./check-perm','Johnson-Meeting2.txt','R','T','karen']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','karen','./check-perm','Johnson-Meeting2.txt','W','F','karen']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','kevin','./check-perm','Johnson-Meeting2.txt','R','T','kevin']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','kevin','./check-perm','Johnson-Meeting2.txt','W','T','kevin']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','tom','./check-perm','Johnson-Meeting2.txt','R','T','tom']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','tom','./check-perm','Johnson-Meeting2.txt','W','F','tom']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','becky','./check-perm','Johnson-Meeting2.txt','R','T','becky']
total+= subprocess.run( args ).returncode
args= ['sudo','-u','becky','./check-perm','Johnson-Meeting2.txt','W','F','becky']
total+= subprocess.run( args ).returncode

print( 'total: ' + str(total) )
