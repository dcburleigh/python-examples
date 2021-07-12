
# assumes your virtualenv root is $HOME/venv 
function topy {
  label_in=$1
  if [[ "$label_in" = "" ]]
  then
     label_in=py3
  fi
  #label=${label_in//[^a-zA-Z0-9_]/}
  label=${label_in//[^a-z0-9]/}
  if [[ "$label" = "$label_in" ]]
  then
    #echo label $label
    bindir=${HOME}/venv/$label/bin
    if [[ ! -d $bindir ]]
    then
       echo ERROR no such directory $bindir
    else
      echo dir $bindir
      deactivate
      source ${bindir}/activate
  fi
  else
    echo ERROR $label_in invalid
  fi
}
