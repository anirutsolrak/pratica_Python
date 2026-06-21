-- Tabela de clientes
create table public.clientes (
    id    bigint generated always as identity primary key,
    nome  text not null,
    email text unique not null
);

-- Tabela de contratos (cada contrato pertence a um cliente)
create table public.contratos (
    id         bigint generated always as identity primary key,
    valor      numeric(12, 2) not null,
    cliente_id bigint not null references public.clientes (id) on delete cascade
);

-- Alguns dados de exemplo para você já praticar consultas
insert into public.clientes (nome, email) values
    ('Ana Souza',    'ana@email.com'),
    ('Bruno Lima',   'bruno@email.com'),
    ('Carla Mendes', 'carla@email.com');

insert into public.contratos (valor, cliente_id) values
    (1500.00, 1),
    (3200.50, 1),
    (980.00,  2);
