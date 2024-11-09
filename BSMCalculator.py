import jax.numpy as jnp
import jax.scipy.stats
from jax import grad

def option_price(S, K, T, r, sigma, q=0.0):
    """
    Dummy Black-Scholes option price function for a European call option.
    Replace with market data or a more complex model if needed.
    """
    d1 = (jnp.log(S / K) + (r - q + 0.5 * sigma**2) * T) / (sigma * jnp.sqrt(T))
    d2 = d1 - sigma * jnp.sqrt(T)
    C = S * jnp.exp(-q * T) * jax.scipy.stats.norm.cdf(d1) - K * jnp.exp(-r * T) * jax.scipy.stats.norm.cdf(d2)
    return C

def dupire_local_volatility(S, T, K, r, q=0.0, sigma=0.2):
    """
    Computes the local volatility using Dupire's equation given the option price function.
    """
    # Define option price function with S and T as variables
    def C(S, T):
        return option_price(S, K, T, r, sigma, q)

    # Compute partial derivatives using JAX's automatic differentiation
    dC_dT = grad(C, argnums=1)(S, T)             # ∂C/∂T
    dC_dS = grad(C, argnums=0)(S, T)             # ∂C/∂S
    d2C_dS2 = grad(grad(C, argnums=0), argnums=0)(S, T)  # ∂²C/∂S²

    # Dupire's equation for local volatility
    numerator = dC_dT + (r - q) * S * dC_dS + q * C(S, T)
    denominator = 0.5 * S**2 * d2C_dS2
    local_volatility = jnp.sqrt(numerator / denominator)
    
    return local_volatility