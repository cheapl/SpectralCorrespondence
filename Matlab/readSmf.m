function [F,X]=readSmf(fname)
%
%
% author: cheapl
% date: 2022/04/27
%
% input: 
%    fname: name of the	SMF data file
%
% output:
%    F: face list
%    X: vertex list
%
% -- this function is used for specCorr3D
%
X=[];
F=[];
fid=fopen(fname,'rt');
while(~feof(fid))
    line=fgetl(fid);
    if(line(1)=='v')
        dd=sscanf(line,'v %f %f %f');
        if(length(dd)==3)
            X=[X;dd];
        end
    elseif(line(1)=='f')
        dd=sscanf(line,'f %d %d %d');
        if(length(dd)==3)
            F=[F;dd];
        end
    end
end
fclose(fid);
X=reshape(X,3,length(X)/3)';
F=reshape(F,3,length(F)/3)';