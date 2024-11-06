with open("./elsa_/lsa/result", "r") as file_:
    next(file_)

    with open("result_0.txt", "w") as file:
        file.write("LS" + "," + "p_value" + "," + "xs" + "," + "ys" + "Len" + "," + "delay" + "\n")
        for line in file_:
            
            nums = list(line.split(","))[2:]
            nums = list(map(float, nums))
            if nums[18] < nums[19]:
                s = str(nums[0]) + "," + str(nums[7]) + "," + \
                str(nums[3]) + "," + str(nums[4]) + "," + str(nums[5]) + "," + str(nums[6]) +"\n"
                file.write(s)

file.close()
file_.close()

with open("./Tes/elsa/lsa/result", "r") as file_:
    next(file_)

    with open("result_0.txt", "a") as file:
        file.write("\n")
        file.write("LS" + "," + "p_value" + "," + "xs" + "," + "ys" + "Len" + "," + "delay" + "\n")
        for line in file_:
            nums = list(line.split("\t"))[2:]
            nums = list(map(float, nums))
            if nums[23] < nums[24]:
                s = str(nums[0]) + "," + str(nums[7]) + "," + \
                str(nums[3]) + "," + str(nums[4]) + "," + str(nums[5]) + "," + str(nums[6]) +"\n"
                file.write(s)

file.close()
file_.close()
