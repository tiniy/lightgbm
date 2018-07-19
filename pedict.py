import json
import numpy as np
import sys

def pred_score(tree, arr):
	if len(tree) == 3:
		return float(tree['leaf_value'])
	split_feature = tree['split_feature']
	default_left = tree['default_left']
	if arr.get(split_feature, None) == None:
		if default_left :
			return pred_score(tree['left_child'], arr)
		else:
			return pred_score(tree['right_child'], arr)
	feature = arr[split_feature]
	decision_type = tree['decision_type']
	if decision_type == "<=" :
		if float(feature) <= float(tree['threshold']):
			return pred_score(tree['left_child'], arr)
		else :
			return pred_score(tree['right_child'], arr)
	elif decision_type == "==":
		cate_fea = tree['threshold'].split("||")
		if feature in cate_fea:
			return pred_score(tree['left_child'], arr)
		else:
			return pred_score(tree['right_child'], arr)

def pred_lgb_score(arr, model_arr):
	score = 0.0
	for model in model_arr:
		shrinkage = float(model['shrinkage'])
		tree = model['tree_structure']
		score += pred_score(tree, arr)
	return 1.0 / (1 + np.exp(-1.0 * score))

model_arr = json.loads(open("model.json").read())['tree_info']

for line in sys.stdin :
	info = line.strip().split()[1:]
	arr = {}
	for e in info :
		k, v = e.split(":")
		arr[int(k)] = v
	print pred_lgb_score(arr, model_arr)
