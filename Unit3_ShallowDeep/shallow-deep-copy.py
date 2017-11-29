# Create source_list
source_list = ['1st_item', ['inner_1', 'inner_2'], '3rd_item']

input("\n________________________ copy() ________________________")
input("copy() preforms a 'shallow' copy;")
input("deeper references are still maintained")
input("copy() is the same as s[:]")
input("(destin_list = source_list[:])")
input("> destin_list = source_list.copy()")
destin_list = source_list.copy()
input("destin_list = "+str(destin_list))

input("\ncopy() contents but addresses NOT copied")
input("hex(id(source_list)) = " + str(hex(id(source_list))))
input("hex(id(destin_list)) = " + str(hex(id(destin_list))))

input("\nAddresses of sublists after copy() - sublist adresses copied!")
input("hex(id(source_list[1])) = " + str(hex(id(source_list[1]))))
input("hex(id(destin_list[1])) = " + str(hex(id(destin_list[1]))))

input("\nTop-level change only to destin_list, ONLY changes destin_list")
destin_list[0] = "***"
input("> destin_list[0] = '***'")
input("source_list = "+str(source_list))
input("destin_list =  "+str(destin_list))

input("\nTop-level change only to source_list, ONLY changes source_list")
source_list[0] = "$$$"
input("> source_list[0] = '$$$'")
input("source_list = "+str(source_list))
input("destin_list =  "+str(destin_list))

input("\n--------------- Change to source changes destin ---------------")

input("\nNote: Addresses of sublists are the same before change...")
input("Addresses of sublists before new object for source_list[1]")
input("hex(id(source_list[1])) = " + str(hex(id(source_list[1]))))
input("hex(id(destin_list[1])) = " + str(hex(id(destin_list[1]))))

input("\nHowever, change item within an item changes BOTH lists")
source_list[1][1] = 'new_inner_2'
input("> source_list[1][1] = 'new_inner_2'")
input("source_list = "+str(source_list))
input("destin_list =  "+str(destin_list))

input("\n---------- Change to source[1] does NOT changes destin ----------")

input("\nTop-level change ONLY changes source_list; New object for source_list[1]")
source_list[1] = ['111', '222']
input("> source_list[1] = ['111', '222']")
input("source_list = "+str(source_list))
input("destin_list =  "+str(destin_list))

input("\nSublist addresses NOT the same after new object for source_list[1]")
input("hex(id(source_list[1])) = " + str(hex(id(source_list[1]))))
input("hex(id(destin_list[1])) = " + str(hex(id(destin_list[1]))))

input("\nNow only source_list is changed because a new object for source_list[1]"
      "\nwas created at line 53.")
source_list[1][1] = '999'
input("> source_list[1][1] = '999'")
input("source_list = "+str(source_list))
input("destin_list =  "+str(destin_list))

input("\n________________________ deepcopy() ________________________")
input("deepcopy() preserves independence;")
input("'deep copy' means recursive copy of contents bu not addressed;")
input("'recursive' means top-level then deeper copies")
input(">from copy import deepcopy (yes you have to import deepcopy)")
from copy import deepcopy

input("\nResetting source_list...")
source_list = ['1st_item', ['inner_1', 'inner_2'], '3rd_item']
destin_list = deepcopy(source_list)
input("> source_list = ['1st_item', ['inner_1', 'inner_2'], '3rd_item']")
input("> destin_list = deepcopy(source_list)")

input("\ndeepcopy() - copies CONTENTS BUT NOT ADDRESSES")
input("Recall that copy() copies sublist addresses")
input("hex(id(source_list)) = " + str(hex(id(source_list))))
input("hex(id(destin_list)) = " + str(hex(id(destin_list))))

input("\nAddresses of sublists are DIFFERENT after deepcopy()")
input("hex(id(source_list[1])) = " + str(hex(id(source_list[1]))))
input("hex(id(destin_list[1])) = " + str(hex(id(destin_list[1]))))

input("\n---- All changes after deepcopy() only apply to target list. ----")

input("\nOnly destin_list[] is changed")
destin_list[0] = "***"
input("> destin_list[0] = '***'")
input("source_list = "+str(source_list))
input("destin_list =  "+str(destin_list))

input("\nOnly source_list[] is changed")
source_list[0] = "$$$"
input("> source_list[0] = '$$$'")
input("source_list = "+str(source_list))
input("destin_list =  "+str(destin_list))

input("\nOnly source_list[] is changed")
source_list[1][1] = 'changed inner 2'
input("> source_list[1][1] = 'changed inner 2'")
input("source_list = "+str(source_list))
input("destin_list =  "+str(destin_list))

input("\nOnly source_list[] is changed")
source_list[1] = ['111', '222']
input("> source_list[1] = ['111', '222']")
input("source_list = "+str(source_list))
input("destin_list =  "+str(destin_list))

input("\nOnly source_list[] is changed")
source_list[1][1] = '999'
input("> source_list[1][1] = '999'")
input("source_list = "+str(source_list))
input("destin_list =  "+str(destin_list))

input("\n____________________ Using Assignment (=) \'copy\' ____________________")

input("\nResetting source_list...")
source_list = ['1st_item', ['inner_1', 'inner_2'], '3rd_item']
input("> source_list = ['1st_item', ['inner_1', 'inner_2'], '3rd_item']")

input("\nAssigning adress of source_list to destin_list")
destin_list = source_list
input("> destin_list = source_list")
input("destin_list = "+str(destin_list))

input("\nBoth identifiers (source_list and destin_list) point to the SAME object in memory")
input("|!| All changes to one effect the other")

input("\nAssigns address of source_list to destin_list")
input("hex(id(source_list)) = " + str(hex(id(source_list))))
input("hex(id(destin_list)) = " + str(hex(id(destin_list))))

input("\nSublists addresses are SAME before new object for source_list[1]")
input("hex(id(source_list[1])) = " + str(hex(id(source_list[1]))))
input("hex(id(destin_list[1])) = " + str(hex(id(destin_list[1]))))

input("\n----- All changes after assignment copy apply to both lists. -----")

input("\nTop-level change changes both source_list and destin_list")
destin_list[0] = "***"
input("> destin_list[0] = '***'")
input("source_list = "+str(source_list))
input("destin_list =  "+str(destin_list))

input("\nTop-level change changes both source_list and destin_list")
source_list[0] = "$$$"
input("> source_list[0] = '$$$'")
input("source_list = "+str(source_list))
input("destin_list =  "+str(destin_list))

input("\nTop-level change changes both source_list and destin_list")
source_list[1] = ['111', '222']
input("> source_list[1] = ['111', '222']")
input("source_list = "+str(source_list))
input("destin_list =  "+str(destin_list))

input("\nSublists addresses are SAME before new object for source_list[1], even AFTER change")
input("hex(id(source_list[1])) = " + str(hex(id(source_list[1]))))
input("hex(id(destin_list[1])) = " + str(hex(id(destin_list[1]))))

input("\nChange item within a sublist changes both lists")
source_list[1][1] = 'new_inner_2'
input("> source_list[1][1] = 'new_inner_2'")
input("source_list = "+str(source_list))
input("destin_list =  "+str(destin_list))
