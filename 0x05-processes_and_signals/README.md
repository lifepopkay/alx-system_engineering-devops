#0x05. Processes and signals

###The following are learnt

##General
* What is a PID
- A PID (i.e., process identification number) is an identification number that is automatically assigned to each process when it is created on a Unix-like operating system.

* What is a process
- A PID (i.e., process identification number) is an identification number that is automatically assigned to each process when it is created on a Unix-like operating system.

* How to find a process’ PID
- Using the ps command

* How to kill a process
- To stop a process in Linux, use the 'kill’ command. kill command sends a signal to the process.

- The PID is needed in order to terminate a frozen or otherwise misbehaving program with the kill command. This command makes it possible to end a program that cannot otherwise be stopped except by rebooting (i.e., restarting) the system, and it is thus an important element in the stability and robustness of Unix-like operating systems.

- kill [option] [pid]

* What is a signal
- signals are software interrupts. They provide a way for the user (or a process) to directly communicate with a process.

- When a signal is sent to a process, the operating system interrupts the normal flow of the process execution and delivers the notification. If the process has previously registered a way to handle that particular signal, that routine is executed, otherwise the system executes the default signal handler.

* What are the 2 signals that cannot be ignored
- SIGKILL(9): it terminate the execution
- SIGNSTOP(19):it stop or pause the execution


##The follwing tasks were completed
- 0-what-is-my-pid
- 1-list_your_processes
- 2-show_your_bash_pid
- 3-show_your_bash_pid_made_easy
- 4-to_infinity_and_beyond
- 5-dont_stop_me_now
- 6-stop_me_if_you_can
- 7-highlander
- 8-beheaded_process
- README.md
