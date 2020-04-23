#!/bin/bash

# create groups
# sudo groupadd Attorneys
# sudo groupadd Law-clerks
# sudo groupadd Paralegals
# sudo groupadd Administrative-assistants

sudo groupadd client-pleading
sudo groupadd client-contract
sudo groupadd calendar-entries
sudo groupadd calendar-meetings
sudo groupadd billings-santana
sudo groupadd billings-jones
sudo groupadd billings-johnson

# assign users to groups
# users Attorneys
# users Law-clerks
# users Paralegals
# users Administrative-assistants

sudo usermod -a -G client-pleading bard 
sudo usermod -a -G client-pleading sam
sudo usermod -a -G client-pleading mary
sudo usermod -a -G client-pleading bob


sudo usermod -a -G client-contract karen 
sudo usermod -a -G client-contract kevin
sudo usermod -a -G client-contract tom
sudo usermod -a -G client-contract becky


sudo usermod -a -G billings-santana bard
sudo usermod -a -G billings-santana karen
sudo usermod -a -G billings-santana sam
sudo usermod -a -G billings-santana kevin
sudo usermod -a -G billings-santana mary
sudo usermod -a -G billings-santana bob

sudo usermod -a -G billings-jones bard
sudo usermod -a -G billings-jones karen
sudo usermod -a -G billings-jones sam
sudo usermod -a -G billings-jones kevin
sudo usermod -a -G billings-jones mary
sudo usermod -a -G billings-jones bob

sudo usermod -a -G billings-johnson bard
sudo usermod -a -G billings-johnson karen
sudo usermod -a -G billings-johnson sam
sudo usermod -a -G billings-johnson kevin
sudo usermod -a -G billings-johnson tom
sudo usermod -a -G billings-johnson becky


# assign a group to each file
# Client docs Attorneys
sudo chgrp client-pleading Jones-Pleading1.txt
sudo chgrp client-pleading Jones-Pleading2.txt
sudo chgrp client-pleading Santana-Pleading1.txt
sudo chgrp client-pleading Santana-Pleading2.txt
sudo chgrp client-contract Johnson-Contract1.txt
sudo chgrp client-contract Johnson-Contract2.txt

# billings  (all personnel)
sudo chgrp billings-santana Jones-Bill1.txt
sudo chgrp billings-santana Jones-Bill2.txt
sudo chgrp billings-santana Santana-Bill1.txt
sudo chgrp billings-santana Santana-Bill2.txt
sudo chgrp billings-jones Jones-Bill1.txt
sudo chgrp billings-jones Jones-Bill2.txt
sudo chgrp billings-jones Santana-Bill1.txt
sudo chgrp billings-jones Santana-Bill2.txt
sudo chgrp billings-johnson Johnson-Bill1.txt
sudo chgrp billings-johnson Johnson-Bill2.txt


# calendar-entries (all personnel)
sudo chgrp calendar-entries Jones-Court1.txt
sudo chgrp calendar-entries Jones-Court2.txt
sudo chgrp calendar-entries Santana-Court1.txt
sudo chgrp calendar-entries Santana-Court2.txt
sudo chgrp calendar-meetings Johnson-Meeting1.txt
sudo chgrp calendar-meetings Johnson-Meeting2.txt

# set permissions on each file

sudo -u bard chmod -R 764 Jones-Pleading1.txt
sudo -u bard chmod -R 764 Jones-Pleading2.txt
sudo -u karen chmod -R 764 Johnson-Contract1.txt
sudo -u karen chmod -R 764 Johnson-Contract2.txt
sudo -u bard chmod -R 764 Santana-Pleading1.txt
sudo -u bard chmod -R 764 Santana-Pleading2.txt

sudo -u sam chmod -R 760 Jones-Bill1.txt
sudo -u sam chmod -R 760 Jones-Bill2.txt
sudo -u kevin chmod -R 760 Johnson-Bill1.txt
sudo -u kevin chmod -R 760 Johnson-Bill2.txt
sudo -u sam chmod -R 760 Santana-Bill1.txt
sudo -u sam chmod -R 760 Santana-Bill2.txt

sudo -u bard chmod -R 744 Jones-Court1.txt
sudo -u mary chmod -R 744 Jones-Court2.txt
sudo -u karen chmod -R 744 Johnson-Meeting1.txt
sudo -u kevin chmod -R 744 Johnson-Meeting2.txt
sudo -u bob chmod -R 744 Santana-Court1.txt
sudo -u bob chmod -R 744 Santana-Court2.txt
