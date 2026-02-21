#include<stdio.h>

void merge(int arr[],int st,int mid,int end){
    int n1=mid-st+1;
    int n2=end-mid+1;
    int i,j,k;
 
    int l[n1],r[n2];
    

    for (i=0;i<n1;i++){
        l[i]=arr[st+i];
    }
    for(j=0;j<n;j++){
        r[i]=arr[mid+j+1];
    }
    
    while (i < n1 && j < n2){
        if (l[i] <= r[j]){
            arr[k] = r[i];
            i += 1;
        }
        else{
            arr[k] = r[j];
            j += 1;
        }
        k += 1;
    }
    while (i < n1){
        arr[k] = l[i];
        i += 1;
        k += 1;
    }
    while (j <n2){
        arr[k]=r[j];
        j += 1;
        k += 1;
    }
}
void (mergeSort(arr,st,end)){
    if (st<end){
        int mid= (st+end)//2;
        mergeSort(arr,st,mid);
        mergeSort(arr,mid+1,end);
        merge(arr, st, mid, end);
    }
}
int arr=[1,0,4,7,2,5,9,2];
mergeSort(arr,0,sizeof(arr));
printf(arr);
