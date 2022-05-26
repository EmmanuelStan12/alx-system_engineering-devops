0-iam_betty -> This script switches the current user to betty
1-who_am_i -> This scripts prints the effective username of the current user
2-groups -> This prints all groups that the current user is part of
3-new_owner ->	This changes the owner of the file hello to betty
4-empty -> This creates an empty file
5-execute -> This adds the execute permission to the owner of the file 'hello'
6-multiple_permissions -> This adds execute permission to the owner and the group owner, and read permission to other users for the file 'hello'
7-everybody -> This adds execute permission to the owner, the group owner and other user for the file 'hello'
8-James_Bond -> This script sets the permission to the owner and group owner to 'no permissions at all' and gives all permissions to other users.
9-John_Doe -> This script sets the mode of the file 'hello' for the owner to '-rwxr-w-wx'
10-mirror_permissions -> This script sets the mode of the file 'hello' to the same as 'olleh'
11-directories_permissions -> This script adds execute permission to all subdirectories of the current directory for the owner, the group owner and all other users except for regular files
12-directory_permissions -> This script creates a directory 'my_dir' with permissions 751 in the working directory
13-change_group -> This script changes the group owner to school for the file 'hello'
100-change_owner_and_group -> This script changes the owner to vincent and the group owner to staff for all files and directories in the working directory
101-symbolic_link_permissions -> This script changes the owner and group owner of the _hello file - A symbolic link to the working directory - to vincent and staff respectively.
102-if_only -> This script changes the owner of the file 'hello' to 'betty' only if it is owned by the user 'guillaume'.
103-Star_Wars -> This script plays Star Wars IV episode in the terminal
