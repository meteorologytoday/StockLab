
function genARMATimeseries(
    c     :: T,
    ϕ     :: Array{T, 1},
    θ     :: Array{T, 1},
    N     :: Integer,
    rand_func
) where T <: AbstractFloat

    p = length(ϕ)
    q = length(θ)

    extra = max(p,q)

    ϕ_T = ϕ'
    θ_T = θ'

    x = zeros(T, extra + N)
    ϵ = zeros(T, extra + N)

    for n = 1 : extra + N
        ϵ[n] = rand_func()
    end
    
    for n = extra + 1 : extra + N
        x[n] = c + ϵ[n] + 
            ( (p > 0) ? ϕ_T * x[n-1:-1:n-p] : 0 ) + ( ( q > 0 ) ? θ_T * ϵ[n-1:-1:n-q] : 0)
    end
    

    return x[ extra + 1 : extra + N ]
end

N = 100
t = collect(1:N)


using PyPlot

fig, ax = plt[:subplots](1, 1, figsize=(12, 8))

for i = 1:50
ax[:plot](t, genARMATimeseries(0.0, [1.0], [1.0, 2.0, 3.0], N, function r(); randn(); end;))
end

plt[:show]()



