function corr = cor(ef1,ef2,x)
%输入m组数据，根据0-x的时间内最大值，对齐m组数据。
x1=ef1(1:1:250000*x,:);x2=ef2(1:1:250000*x,:);
p=zeros([1 2]);
[m1,p(1)]=max(x1);[m2,p(2)]=max(x2);
pmin=min(p);
emm=ef1((p(1)-pmin+1):1:(p(1)-pmin+1)+699999);
he=ef2((p(2)-pmin+1):1:(p(2)-pmin+1)+699999);
corr=corr2(emm,he);
end