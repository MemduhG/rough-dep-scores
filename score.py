def get_head(token):
	return token.split("\t")[-4]

def get_dep(token):
	return token.split("\t")[-3]

def scores(tfile,pfile): 
	test= []
	pred = []

	with open(tfile,"r",encoding="utf-8") as testfile:
		for item in testfile:
			if "#" not in item:
				test.append(item)

	with open(pfile,"r",encoding="utf-8") as testfile:
		for item in testfile:
			if "#" not in item:
				pred.append(item)

	print(len(test))
	print(len(pred))

	counter = 0


	uas = 0.0
	las = 0.0
	token = 0

	dep_type = []
	for item in test:
		if "\t_\t_" not in item:
			continue
		temp = get_dep(item)
		if temp not in dep_type and "_" not in temp:
			dep_type.append(temp)

	print(dep_type)
	print(len(dep_type))

	dep_count = {}
	dep_stats = {}

	for item in dep_type:
		dep_stats[item] = [0,0]
		dep_count[item] = 0

	for i in range(len(test)):
		if(len(test[i].split("\t"))<5):
			continue
		if("\t_\t_" not in test[i] or "_" in get_dep(test[i]) or "_" in get_head(test[i])):
			continue
		token +=1
		dep_count[get_dep(test[i])]+=1
		if get_head(test[i]) == get_head(pred[i]):
			uas += 1
			dep_stats[get_dep(test[i])][0]+=1
		if get_dep(test[i]) == get_dep(pred[i]) and get_head(test[i]) == get_head(pred[i]):
			las += 1
			dep_stats[get_dep(test[i])][1]+=1
		
	print("UAS: " + str(uas/token) + ", LAS: " + str(las/token))

	for item in dep_type:
		unlab = float(dep_stats[item][0])/dep_count[item]
		lab = float(dep_stats[item][1])/dep_count[item]
		print(item + " UAS: " + str(unlab) + ", LAS: " + str(lab))

