function mergeSort(arr) {
	if(arr.length < 2) {
		return arr;
	}
	const middleIndex = Math.floor(arr.length / 2);
	const leftArr = arr.slice(0, middleIndex);
	const rightArr = arr.slice(middleIndex ,arr.length);

	
}