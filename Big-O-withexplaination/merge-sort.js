function mergeSort(arr) {
	if(arr.length < 2) {
		return arr;
	}
	const middleIndex = Math.floor(arr.length / 2);
	const leftArr = arr.slice(0, middleIndex);
	const rightArr = arr.slice(middleIndex ,arr.length);

 	return merge(mergeSort(leftArr),mergeSort(rightArr))
	
}

function merge(leftArr,rightArr) {
	let resultArr =[];
	let leftIndex = 0;
	let rightIndex = 0;

	while (leftIndex < leftArr.length && rightIndex < rightArr.length) {
		if (leftArr[leftIndex] < resultArr[rightIndex]) {
			resultArr.push(leftArr[leftIndex]);
			leftIndex +=1; 
		} else {
			resultArr.push(rightArr[rightIndex]);
			rightIndex +=1;
		}
	}
	return resultArr.concat(leftArr.slice(leftIndex)).concat(rightArr.slice(rightIndex));
}


var arr =[3,34,33,4,5,1,0];
console.log(mergeSort(arr))