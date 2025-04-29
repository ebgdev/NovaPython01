# pwd : print working directory
# ls : list
# cd : change directory
# mkdir : make directory

# system 
# global
# local 
# 
# \r\n

# git --version
# git -v

# git config --help
# git config -h

# git config --global user.name "irfan bahcivan"

# git config --global user.email git_projesi@ptct.net

# git config --global core.editor "code --wait"

# git config --global core.autocrlf true/input
# true for win
# input for mac/linux

# git config --global -e


# git init ---> create git repo in local

# git branch -m main # change the branch name from master to main

# rm -rf .git/ --> to delete repo 

# LOCAL (directory   ---> staging ---> commited ) ||| (REMOTE(github/cloud))

# echo hello > file1.txt # file1.txt ye hello mesajini yazdirir

# git add . --> directory de ne varsa staging area ekler

# git add *.txt --> (pattern) sadece .txt uzantili dosyalari ekler

# git add file1.txt --> sadece file1.txt ekler

# echo merhaba > file2.txt

# git commit -m "mesaj"

# her commit
# 1 - ID
# 2 - Message
# 3 - Date/Time
# 4 - Author(yazar)
# 5 - Complete Snapshot

# touch file3.txt

# cat dosya.txt --> sadece dosyanin icini gosterir.

# git status --> general way
# git status -s --> summrized way

# _s_ _w_ example.txt
# s for staging area
# w for working directory

# M : modified
# A : added
# D : deleted  
# ?? : untrackted file

# ls --> show working direcotoy's files
# git ls-files --> shows staging area's files

# touch .gitignore --> ignore yapmak istedigimiz elemanlari ekleriz

# rm komutu sadece working directory'den siler sonra git add . ile degisiklikleri eklememiz gerekli.
# git rm file_name.py --> hem workig directory'den hem de staging area'dan dosyayi siler


# git commit 
# --> bir panel acilir ve orada detayli veya uzun mesaj yazabiliriz. (kaydet-kapat)

# mv first_name.txt second_name.py

# git diff --> working directory ve staging area arasindaki farki gosterir
# git diff --staged --> commit'ler ve staging area arasindaki farki gosterir.

# --------------------------------

# git config --global diff.tool vscode
# git config --global difftool.vscode.cmd "code --wait --diff $LOCAL $REMOTE"
# bu komutlardan sonra git config --gobal -e

# EX : 
# [user]
# 	name = irfan bahcivan
# 	email = git_projesi@ptct.net
# [core]
# 	editor = code --wait
# 	autocrlf = true
# [diff]
# 	tool = vscode
# [difftool "vscode"]
# 	cmd = "code --wait --diff $LOCAL $REMOTE"

# --------------------------------

# git difftool --> (vscode'da) working directory ve staging area arasindaki farki gosterir
# git difftool --staged --> (vscode'da) commit'ler ve staging area arasindaki farki gosterir.

# ---------------

# git log 
# ---neler gosterir---
# commit hash_id
# author - email
# Date and Time
# messaje

# ---------------

# git log --oneline

# git log --oneline --reverse

# ---------------
# viewing commit:

# git show head

# git show head~4

# git show head~10:file2.txt:specific_file_name.txt

# git show ---commit_id---

# ---------------

# git ls-tree --> files and dirs in commited area
# blob --> file (dosya)
# tree --> directory (klasor)
# commit
# tags 

# ---------------
# unstaging

# git restore --staged hello.py --> staging area'dan temizler
# git restore . --> working directory'den temizler

# ----------------

# deleting untracked files or directories

# git clean -f --> unrackted files(dosyalar)
# git clean -fd --> untracked directories(klasorler)

# ----------------
# restoring a file to an earlier version

# step1:
# git rm example.txt
# git commit -m "example.txt is deleted"

# step2:
# git restore --source=head~1(could be any number) example.txt

# git status -s
# --> ?? example.txt

# step3 : 
# git add .
# git commit -m "example.txt get restored."

# -----------------------------
# git log --oneline --stat
# git log --oneline --patch
# git log --oneline -3 (son 3 taneyi gosterir)
# git log --oneline --patch -3

# git log --oneline -i -S"palindorme"
# hangi commitlerde palindorme fonksiyonu , palindorme variable ismi veya kodu veya commit aciklamasinda gectiyse hepsini gosterir.
# -----------------------------


# # git aliases odevi

# git log --oneline --patch

# git lg


# -------------------------
# formating the log output:
# git log --pretty=format:"hello %an"

# git log --pretty=format:"%an commited %H"

# %H --> commited hash
# %h --> commited abbrevated hash
# %T --> tree hash
# %t --> abbrevated tree hash
# %P --> parent hashes
# %p --> abbrevated parent hashes
# %an --> author name
# %ae --> author email
# %cd --> commiter date

# git log --pretty=format:"%an commited %h on %cd"

# git log --pretty=format:%Cgreen%an commited%h on %cd"


# -------------------------
# git aliases

# git config --global alias.lg"log --pretty=format:'%an commited %h'"

# veya

# git config --global alias.lg"log --oneline --all --graph" --> git lg

# git config --global alias.unstage"restore --staged" --> git unstage

# -----------------------------
# viewing a commit.

# git show head~2

# git show head..head~2

# git show head~2 --name-only --> to see the file name/names that are changed

# git show head~2 --name-status

# git show head~2 <file-name.ex>

# -----------------------------
# cheking out a commit

# git checkout <commit-id>

# git checkout <branch-name> ex: git checkout main/master



# -----------------------------

# git bisect start 

# git bisect bad

# git bisect good/bad

# git bisect reset


# -------------------------
# finding contributers 

# git shortlog 

# - s -> summary
# - n -> numberd (kim en cok commit yaptiysa basta gelir)
# - e -> email

# git shortlog -s -n -e

# git shortlog -s -e -n --before="2025-04-24"

# -------------------------

# restoring file second approach:

# git rm -f (if needed) <file_name>

# git add , commit

# git checkout head~1 <deleted_file_name>

# by git status -s --> (A_ <file_name>)

# git commit -m "<file_name> get restored via checkout"

# -------------------------

# git show v1.0 --commit_id-- (light weight tagging)

# git checkout v1.0
# git show v1.0

# git tag -a v1.1 -m "few updates and sign-in-bugfix" <commit-id> (annotation tagging)

# git tag --> to list all tages

# git tag -n --> to see tags with there messages

# git tag -d v1.0 --> to drop(delete) a tag


# -------------------------


