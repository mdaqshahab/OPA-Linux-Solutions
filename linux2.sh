#!/bin/bash
cat $1 > abc
grep -v '^I' abc |
awk 'BEGIN{FS=",";choice;count;i}
     { if(NR==1) 
       {choice=$3; a[i++]=$3}
       else{
            a[i++]=$3;
            if(choice>$3) {choice=$3;}
            }
    }
    END{ for(j=0;j<i;j++)
        {
           if(a[j]==choice){
             count++;
            }
        }
        {print count}
    }' 
    
# #!/bin/bash
# cat opa_may_15.data | grep -v "^I" | sort -k 3 -t ',' > file
# MIN=$(cut -d ',' -f3 file | head -1)
# COUNT=0
# for LINE in $(cat file)
# do
#         IFS=',' read -r -a ARR <<< "$LINE"
#         if [[ "${ARR[2]}" -eq "$MIN" ]]
#         then
#                 (( COUNT++ ))
#         fi
# done
# echo "$COUNT"