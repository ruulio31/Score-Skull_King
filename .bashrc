# .bashrc

# Source global definitions
if [ -f /etc/bashrc ]; then
	. /etc/bashrc
fi

# Uncomment the following line if you don't like systemctl's auto-paging feature:
# export SYSTEMD_PAGER=

# User specific aliases and functions
export PATH=/home/mydev/dev/pycharm-community-2019.1.1/bin:$PATH
export PATH=/home/mydev/dev/android-studio/bin:$PATH
export PATH=/home/mydev/Android/Sdk/tools:$PATH
export PATH=/home/mydev/Android/Sdk/tools/bin:$PATH
export PATH=/home/mydev/Android/Sdk/platform-tools:$PATH
#export PATH=/home/mydev/dev/android-studio/bin/sdk:$ANDROID_SDK_HOME
alias ll='ls -lha'
alias c='clear'
