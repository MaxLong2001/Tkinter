function [replaced] = replaceInf(y)

y(find(isinf(y)))=NaN;

a= ones(size(y)+2);

a(find(a==1))=NaN;

a(2:end-1,2:end-1)=y;

[r,c]=find(isnan(a(2:end-1,2:end-1)));

for i = 1:length(r)

a(r(i)+1,c(i)+1) = nanmean(reshape(a(r(i):r(i)+2,c(i):c(i)+2),1,[]));

end

replaced = a(2:end-1,2:end-1);