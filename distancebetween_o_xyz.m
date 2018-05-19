% optimization there are 2 optimization function GD grandient descent; annealing
% first to definme the boundary condition z:plate z=4 o: point(0,0,0) 
% and define what is the optimization function the distance between the point o
% and the z so which is the shortest point between z o
% we define the optimization function optim(point on the z plate)
function [optim] = optim(x,y,z)
% calculate the distance between (x,y,z) (0,0,0)
optim = sqrt(x*x + y*y + z*z)
end


