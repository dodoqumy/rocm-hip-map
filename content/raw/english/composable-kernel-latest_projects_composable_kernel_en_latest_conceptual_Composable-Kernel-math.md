---
title: "Composable Kernel mathematical basis &#8212; Composable Kernel 1.2.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/composable_kernel/en/latest/conceptual/Composable-Kernel-math.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T21:10:37.124294+00:00
content_hash: "511f6048bb9f57d5"
---

# Composable Kernel mathematical basis

This is an introduction to the math which underpins the algorithms implemented in Composable Kernel.

For vectors \(x^{(1)}, x^{(2)}, \ldots, x^{(T)}\) of size \(B\) you can decompose the
softmax of concatenated \(x = [ x^{(1)}\ | \ \ldots \ | \ x^{(T)} ]\) as,

\begin{align}
m(x) & = m( [ x^{(1)}\ | \ \ldots \ | \ x^{(T)} ] ) = \max( m(x^{(1)}),\ldots, m(x^{(T)}) ) \\
f(x) & = [\exp( m(x^{(1)}) - m(x) ) f( x^{(1)} )\ | \ \ldots \ | \ \exp( m(x^{(T)}) - m(x) ) f( x^{(T)} )] \\
z(x) & = \exp( m(x^{(1)}) - m(x) )\ z(x^{(1)}) + \ldots + \exp( m(x^{(T)}) - m(x) )\ z(x^{(1)}) \\
\operatorname{softmax}(x) &= f(x)\ / \ z(x)
\end{align}

where \(f(x^{(j)}) = \exp( x^{(j)} - m(x^{(j)}) )\) is of size \(B\) and
\(z(x^{(j)}) = f(x_1^{(j)})+ \ldots+ f(x_B^{(j)})\) is a scalar.

For a matrix \(X\) composed of \(T_r \times T_c\) tiles, \(X_{ij}\), of size
\(B_r \times B_c\) you can compute the row-wise softmax as follows.

For \(j\) from \(1\) to \(T_c\), and \(i\) from \(1\) to \(T_r\) calculate,

\begin{align}
\tilde{m}_{ij} &= \operatorname{rowmax}( X_{ij} ) \\
\tilde{P}_{ij} &= \exp(X_{ij} - \tilde{m}_{ij} ) \\
\tilde{z}_{ij} &= \operatorname{rowsum}( P_{ij} ) \\
\end{align}

If \(j=1\), initialize running max, running sum, and the first column block of the output,

\begin{align}
m_i &= \tilde{m}_{i1} \\
z_i &= \tilde{z}_{i1} \\
\tilde{Y}_{i1} &= \diag(\tilde{z}_{ij})^{-1} \tilde{P}_{i1}
\end{align}

Else if \(j>1\),

Update running max, running sum and column blocks \(k=1\) to \(k=j-1\)


\begin{align}
m^{new}_i &= \max(m_i, \tilde{m}_{ij} ) \\
z^{new}_i &= \exp(m_i - m^{new}_i)\ z_i + \exp( \tilde{m}_{ij} - m^{new}_i )\ \tilde{z}_{ij} \\
Y_{ik} &= \diag(z^{new}_{i})^{-1} \diag(z_{i}) \exp(m_i - m^{new}_i)\ Y_{ik}
\end{align}

Initialize column block \(j\) of output and reset running max and running sum variables:


\begin{align}
\tilde{Y}_{ij} &= \diag(z^{new}_{i})^{-1} \exp(\tilde{m}_{ij} - m^{new}_i ) \tilde{P}_{ij} \\
z_i &= z^{new}_i \\
m_i &= m^{new}_i \\
\end{align}
