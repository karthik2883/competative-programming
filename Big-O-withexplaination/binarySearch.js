var arr = [];
var start = 0;

for(var i =1; i<=300; i++) {
	 arr.push(i);
}


var end = arr.length -1;
var target = 125;

function binarySearch(arr,start,end,target) {
	console.log(arr.slice(start,end));
		
	if(start > end) return false;

    var midIndex = Math.floor((start + end)/2);
	
	if(arr[midIndex] === target) return true;
	
	if(arr[midIndex]>target) return binarySearch(arr,start,midIndex-1,target);
	else return binarySearch(arr,midIndex+1,end,target);


}
console.log(binarySearch(arr,start,end,target))
