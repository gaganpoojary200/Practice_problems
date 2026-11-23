def TowerofHanoi(n,source,dest,aux):
    if n==0:
        return
    TowerofHanoi(n-1,source,aux,dest)
    print("Disk ",n,"moved from ",source,"to ",dest)
    TowerofHanoi(n-1,aux,dest,source)
if __name__=="__main__":
    n=3
    TowerofHanoi(n,'A','C','B')