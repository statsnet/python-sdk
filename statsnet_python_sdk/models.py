# generated by datamodel-codegen:
#   filename:  swagger.yaml
#   timestamp: 2024-05-08T13:02:55+00:00

from __future__ import annotations

from typing import Any, Dict, List, Union

from typing_extensions import NotRequired, TypedDict


class Identifier(TypedDict):
    type: NotRequired[str]
    value: NotRequired[str]


class MainIndustryCodeItem(TypedDict):
    code: NotRequired[str]
    description: NotRequired[str]
    is_main: NotRequired[bool]


class MainIndustryCode(TypedDict):
    code: NotRequired[str]
    description: NotRequired[str]
    is_main: NotRequired[bool]


class ParentIndustryCode(TypedDict):
    main_industry_code: NotRequired[str]
    key: NotRequired[str]
    industry_codes: NotRequired[List[ParentIndustryCode]]


class QuasiContracts(TypedDict):
    id: NotRequired[int]
    lot_id: NotRequired[int]
    lot_name: NotRequired[str]
    status: NotRequired[str]
    advert_id: NotRequired[int]
    advert_name: NotRequired[str]
    customer_identifier: NotRequired[str]
    customer_name: NotRequired[str]
    count: NotRequired[float]
    price: NotRequired[float]
    supplier_name: NotRequired[str]
    supplier_identifier: NotRequired[str]
    date: NotRequired[str]
    source_url: NotRequired[str]
    source: NotRequired[str]
    total: NotRequired[int]


class QuasiContractsWithMeta(TypedDict):
    quasi_contracts: NotRequired[List[QuasiContracts]]
    total: NotRequired[int]
    pagination_total: NotRequired[int]
    pagination_offset: NotRequired[int]


class DataView(TypedDict):
    key: NotRequired[str]
    value: NotRequired[str]


class DataViewResult(TypedDict):
    scoring: NotRequired[DataView]
    shareholders: NotRequired[DataView]
    officers: NotRequired[DataView]
    certs: NotRequired[DataView]
    conformity_certs: NotRequired[DataView]
    intellectual_properties: NotRequired[DataView]
    events: NotRequired[DataView]
    debtors: NotRequired[DataView]
    stores: NotRequired[DataView]
    jobs: NotRequired[DataView]
    trademarks: NotRequired[DataView]
    quasi_contracts: NotRequired[DataView]
    pos_terminals: NotRequired[DataView]
    places: NotRequired[DataView]
    bank_accounts: NotRequired[DataView]
    marketplaces: NotRequired[DataView]
    counterparties: NotRequired[DataView]
    websites: NotRequired[DataView]
    gov_loans: NotRequired[DataView]
    farmers: NotRequired[DataView]
    names: NotRequired[DataView]
    court_cases: NotRequired[DataView]
    employees: NotRequired[DataView]
    shareholders_by_count: NotRequired[DataView]
    officers_by_count: NotRequired[DataView]
    registries: NotRequired[DataView]


class Officer(TypedDict):
    name: NotRequired[str]
    name_en: NotRequired[str]
    name_native: NotRequired[str]
    role: NotRequired[str]
    start_date: NotRequired[str]
    end_date: NotRequired[str]
    inactive: NotRequired[bool]


class Identifier2(TypedDict):
    type: str
    value: NotRequired[str]


class ListItem(TypedDict):
    user_id: NotRequired[int]
    name: NotRequired[str]
    id: NotRequired[int]
    org_id: NotRequired[int]
    created_at: NotRequired[str]
    deleted_at: NotRequired[str]


class FavouriteListResponse(TypedDict):
    pagination_offset: NotRequired[int]
    pagination_total: NotRequired[int]
    list: NotRequired[List[ListItem]]


class ListItem1(TypedDict):
    org_id: NotRequired[int]
    user_id: NotRequired[int]
    status: NotRequired[str]
    created_at: NotRequired[str]
    deleted_at: NotRequired[str]


class OrganizationInvitesResponse(TypedDict):
    pagination_offset: NotRequired[int]
    pagination_total: NotRequired[int]
    list: NotRequired[List[ListItem1]]


class OrganizationResponse(TypedDict):
    id: NotRequired[int]
    name: NotRequired[str]
    tax_id: NotRequired[str]
    billing_address: NotRequired[str]
    jurisdiction: NotRequired[str]
    owner_user_id: NotRequired[str]
    owner_user_email: NotRequired[str]
    owner_user_name: NotRequired[str]
    created_at: NotRequired[str]
    updated_at: NotRequired[str]
    deleted_at: NotRequired[str]
    start_date: NotRequired[str]
    end_date: NotRequired[str]
    next_bill_date: NotRequired[str]
    reports: NotRequired[str]
    plan_id: NotRequired[str]


class PlanResponse(TypedDict):
    id: NotRequired[int]
    plan: NotRequired[str]
    price: NotRequired[int]
    currency: NotRequired[str]
    reports: NotRequired[int]
    alternative: NotRequired[int]


class Filters1(TypedDict):
    jurisdiction: NotRequired[List[str]]
    structure: NotRequired[List[str]]
    company_size: NotRequired[List[str]]
    main_industry_code: NotRequired[List[str]]
    inactive: NotRequired[List[bool]]
    state: NotRequired[List[str]]
    query: NotRequired[str]
    limit: NotRequired[List[str]]
    true_limit: NotRequired[int]


class Filters(TypedDict):
    type: NotRequired[str]
    file_type: NotRequired[str]
    filters: NotRequired[Filters1]


class ExportItem(TypedDict):
    id: NotRequired[int]
    user_id: NotRequired[int]
    filters: NotRequired[Filters]
    fields: NotRequired[List[str]]
    type: NotRequired[str]
    status: NotRequired[str]
    chargeable: NotRequired[bool]
    balance_reserved: NotRequired[bool]
    file_path: NotRequired[str]
    file_name: NotRequired[str]
    file_type: NotRequired[str]
    created_at: NotRequired[str]
    updated_at: NotRequired[str]
    error: NotRequired[str]
    language: NotRequired[str]
    hash_id: NotRequired[str]
    url: NotRequired[str]
    description: NotRequired[str]


class ExportResult(TypedDict):
    export: NotRequired[List[ExportItem]]
    total: NotRequired[int]
    pagination_count: NotRequired[int]
    pagination_offset: NotRequired[int]


class TokensResponse(TypedDict):
    access_token: NotRequired[str]
    refresh_token: NotRequired[str]
    expire_at: NotRequired[str]


class UserResponse(TypedDict):
    id: NotRequired[int]
    name: NotRequired[str]
    company_name: NotRequired[str]
    position: NotRequired[str]
    role: NotRequired[str]
    email: NotRequired[str]
    email_verified: NotRequired[str]
    phone: NotRequired[str]
    phone_verified: NotRequired[str]
    language: NotRequired[str]
    created_at: NotRequired[str]
    updated_at: NotRequired[str]
    deleted_at: NotRequired[str]
    plan_id: NotRequired[int]
    reports: NotRequired[int]
    start_date: NotRequired[str]
    end_date: NotRequired[str]
    next_bill_date: NotRequired[str]
    api_token: NotRequired[str]
    email_delivery_ability: NotRequired[str]
    status: NotRequired[str]
    last_sign_in_date: NotRequired[str]


class Area(TypedDict):
    name: NotRequired[str]
    path: NotRequired[str]
    name_en: NotRequired[str]
    name_native: NotRequired[str]


class LocationResponse(TypedDict):
    jurisdiction: NotRequired[str]
    areas: NotRequired[List[Area]]
    name_ru: NotRequired[str]
    name_en: NotRequired[str]


class GovernmentContractItem(TypedDict):
    supplier_biin: NotRequired[str]
    supplier_bik: NotRequired[str]
    supplier_iik: NotRequired[str]
    supplier_bank_name_kz: NotRequired[str]
    supplier_bank_name_ru: NotRequired[str]
    customer_bin: NotRequired[str]
    customer_bik: NotRequired[str]
    customer_iik: NotRequired[str]
    customer_bank_name_kz: NotRequired[str]
    customer_bank_name_ru: NotRequired[str]
    sign_reason_doc_name: NotRequired[str]
    supplier_name: NotRequired[str]
    customer_name: NotRequired[str]
    customer_statsnet_id: NotRequired[str]
    supplier_statsnet_id: NotRequired[str]
    description_kz: NotRequired[str]
    description_ru: NotRequired[str]
    contract_sum_wnds: NotRequired[float]
    sign_date: NotRequired[str]
    ec_end_date: NotRequired[str]


class GovContractsWithMeta(TypedDict):
    count: NotRequired[int]
    pagination_count: NotRequired[int]
    pagination_offset: NotRequired[int]
    government_contract: NotRequired[List[GovernmentContractItem]]


class Identifier3(TypedDict):
    type: NotRequired[str]
    value: NotRequired[str]


class Address(TypedDict):
    raw: NotRequired[str]
    state: NotRequired[str]


class CompanyItem1(TypedDict):
    id: NotRequired[str]
    title: NotRequired[str]
    identifiers: NotRequired[List[Identifier3]]
    name: NotRequired[str]
    name_en: NotRequired[str]
    inactive: NotRequired[bool]
    jurisdiction: NotRequired[str]
    addresses: NotRequired[List[Address]]
    structure: NotRequired[str]


class Search(TypedDict):
    company: NotRequired[List[CompanyItem1]]
    count: NotRequired[int]
    pagination_count: NotRequired[int]
    pagination_offset: NotRequired[int]
    is_phone: NotRequired[bool]


class Node(TypedDict):
    id: NotRequired[int]
    name: NotRequired[str]
    type: NotRequired[str]
    identifier: NotRequired[str]
    key: NotRequired[str]


class Link(TypedDict):
    source_identifier: NotRequired[str]
    source_name: NotRequired[str]
    source_key: NotRequired[int]
    company_id: NotRequired[int]
    company_name: NotRequired[str]
    company_identifier: NotRequired[str]
    company_key: NotRequired[int]
    connection: NotRequired[str]


class AffiliationLink(TypedDict):
    source_identifier: NotRequired[str]
    source_name: NotRequired[str]
    source_key: NotRequired[int]
    company_id: NotRequired[int]
    company_name: NotRequired[str]
    company_identifier: NotRequired[str]
    company_key: NotRequired[int]
    connection: NotRequired[str]


class MetaItem(TypedDict):
    connection: NotRequired[str]
    count: NotRequired[int]


class FizRelations(TypedDict):
    nodes: NotRequired[List[Node]]
    links: NotRequired[List[Link]]
    affiliation_links: NotRequired[List[AffiliationLink]]
    meta: NotRequired[List[MetaItem]]


class Contact(TypedDict):
    value: str


class Meta(TypedDict):
    old_shareholder_count: NotRequired[int]
    new_shareholder_count: NotRequired[int]
    old_officer_count: NotRequired[int]
    new_officer_count: NotRequired[int]


class GovContractsMetaItem(TypedDict):
    sum: NotRequired[float]
    year: NotRequired[int]
    count: NotRequired[int]
    method: NotRequired[str]


class GovApplicationsMetaItem(TypedDict):
    sum: NotRequired[float]
    year: NotRequired[int]
    count: NotRequired[int]


class QuasiContractsMetaItem(TypedDict):
    sum: NotRequired[float]
    year: NotRequired[int]
    count: NotRequired[int]


class ContractsMeta(TypedDict):
    company_id: NotRequired[int]
    gov_contracts_meta: NotRequired[List[GovContractsMetaItem]]
    gov_applications_meta: NotRequired[List[GovApplicationsMetaItem]]
    quasi_contracts_meta: NotRequired[List[QuasiContractsMetaItem]]


class Registry(TypedDict):
    end_date: NotRequired[str]
    inclusion_reason: NotRequired[str]
    jurisdiction: NotRequired[str]
    name: NotRequired[str]
    registry_name: NotRequired[str]
    source: NotRequired[str]
    start_date: NotRequired[str]


class View(TypedDict):
    activities: NotRequired[int]
    bank_accounts: NotRequired[int]
    certs: NotRequired[int]
    companies_contacts: NotRequired[int]
    counterparties: NotRequired[int]
    court_cases: NotRequired[int]
    debtors: NotRequired[int]
    debtors_amount: NotRequired[float]
    employees: NotRequired[int]
    employment_contracts: NotRequired[int]
    events: NotRequired[int]
    gov_contracts: NotRequired[int]
    gov_loans: NotRequired[int]
    id: NotRequired[int]
    intellectual_properties: NotRequired[int]
    jobs: NotRequired[int]
    marketplaces: NotRequired[int]
    names: NotRequired[int]
    officers: NotRequired[int]
    officers_by_count: NotRequired[str]
    places: NotRequired[int]
    pos_terminals: NotRequired[int]
    procurement: NotRequired[int]
    quasi_contracts: NotRequired[int]
    registries: NotRequired[List[Registry]]
    shareholders: NotRequired[int]
    shareholders_by_count: NotRequired[str]
    social_networks: NotRequired[int]
    stores: NotRequired[int]
    subsidiaries: NotRequired[int]
    trademarks: NotRequired[int]
    websites: NotRequired[int]


class Registration(TypedDict):
    name: NotRequired[str]
    short_name: NotRequired[str]
    reg_status: NotRequired[str]
    reg_department: NotRequired[str]
    creation_method: NotRequired[str]
    typical_character: NotRequired[str]
    non_profit: NotRequired[bool]
    foreign_invert: NotRequired[bool]
    enterprise: NotRequired[bool]
    enterprise_type: NotRequired[bool]
    international: NotRequired[bool]
    branches_existence: NotRequired[bool]
    ownership_type: NotRequired[str]
    without_citizenship: NotRequired[str]
    founders_count: NotRequired[int]


FieldsTypesSummary2023Item = TypedDict(
    "FieldsTypesSummary2023Item",
    {
        "title": NotRequired[str],
        "square": NotRequired[str],
        "Кол-во СХТП": NotRequired[str],
        "Кол-во полей": NotRequired[str],
    },
)


FieldsCropSummary2023Item = TypedDict(
    "FieldsCropSummary2023Item",
    {
        "title": NotRequired[str],
        "square": NotRequired[str],
        "Кол-во СХТП": NotRequired[str],
        "Кол-во полей": NotRequired[str],
    },
)


class Farmer(TypedDict):
    name: NotRequired[str]
    officer_name: NotRequired[str]
    state: NotRequired[str]
    fields_types_summary_2023: NotRequired[List[FieldsTypesSummary2023Item]]
    fields_crop_summary_2023: NotRequired[List[FieldsCropSummary2023Item]]
    source_url: NotRequired[str]


class ConfCert(TypedDict):
    start_date: NotRequired[str]
    end_date: NotRequired[str]
    registration_number: NotRequired[str]
    product_name: NotRequired[str]
    source: NotRequired[str]
    source_url: NotRequired[str]
    cert_issuer: NotRequired[str]
    producer_name: NotRequired[str]
    declarant_name: NotRequired[str]


class Excise(TypedDict):
    start_date: NotRequired[str]
    end_date: NotRequired[str]
    status: NotRequired[str]
    product: NotRequired[str]
    excise_code: NotRequired[str]
    object: NotRequired[str]
    address: NotRequired[str]


class BankAccount(TypedDict):
    bank_bic: NotRequired[str]
    bank_name: NotRequired[str]
    created_at: NotRequired[str]
    date_open: NotRequired[str]
    holder: NotRequired[str]
    iban: NotRequired[str]
    id: NotRequired[int]
    identifier: NotRequired[str]
    jurisdiction: NotRequired[str]
    type: NotRequired[str]
    updated_at: NotRequired[str]


class Store(TypedDict):
    address: NotRequired[str]
    company_identifier: NotRequired[str]
    created_at: NotRequired[str]
    id: NotRequired[int]
    jurisdiction: NotRequired[str]
    license: NotRequired[str]
    name: NotRequired[str]
    store_name: NotRequired[str]
    updated_at: NotRequired[str]


class Cert(TypedDict):
    agency: NotRequired[str]
    applicant_address: NotRequired[str]
    applicant_contacts: NotRequired[List[str]]
    applicant_desc: NotRequired[str]
    applicant_identifier: NotRequired[str]
    applicant_origin: NotRequired[str]
    comment: NotRequired[str]
    created_at: NotRequired[str]
    doc_type: NotRequired[str]
    end_date: NotRequired[str]
    hs_code: NotRequired[str]
    id: NotRequired[int]
    issue_date: NotRequired[str]
    jurisdiction: NotRequired[str]
    number: NotRequired[str]
    producer_address: NotRequired[str]
    producer_contacts: NotRequired[List[str]]
    producer_desc: NotRequired[str]
    producer_identifier: NotRequired[str]
    producer_origin: NotRequired[str]
    product_name: NotRequired[str]
    source: NotRequired[str]
    start_date: NotRequired[str]
    status: NotRequired[str]
    updated_at: NotRequired[str]


class Debtor(TypedDict):
    count: NotRequired[int]
    recoverer_identifier: NotRequired[str]
    sum: NotRequired[float]


class Job(TypedDict):
    company_id: NotRequired[int]
    company_url: NotRequired[str]
    education: NotRequired[str]
    experience: NotRequired[str]
    id: NotRequired[int]
    identifier: NotRequired[str]
    industry: NotRequired[str]
    internship: NotRequired[str]
    job_type: NotRequired[str]
    salary: NotRequired[str]
    start_date: NotRequired[str]
    title: NotRequired[str]
    work_schedule: NotRequired[str]
    work_terms: NotRequired[str]


class QuasiContract(TypedDict):
    advert_id: NotRequired[int]
    advert_name: NotRequired[str]
    count: NotRequired[float]
    customer_identifier: NotRequired[str]
    customer_name: NotRequired[str]
    date: NotRequired[str]
    id: NotRequired[int]
    lot_id: NotRequired[int]
    lot_name: NotRequired[str]
    price: NotRequired[float]
    source: NotRequired[str]
    source_url: NotRequired[str]
    status: NotRequired[str]
    supplier_identifier: NotRequired[str]
    supplier_name: NotRequired[str]


class Place(TypedDict):
    address: NotRequired[str]
    area: NotRequired[str]
    city: NotRequired[str]
    contacts: NotRequired[List[str]]
    district: NotRequired[str]
    foursquare: NotRequired[str]
    from_: NotRequired[str]
    heading: NotRequired[str]
    home_number: NotRequired[str]
    id: NotRequired[int]
    index: NotRequired[str]
    latitude: NotRequired[str]
    livejournal: NotRequired[str]
    longitude: NotRequired[str]
    name: NotRequired[str]
    street_name: NotRequired[str]
    subheading: NotRequired[str]
    time_work: NotRequired[str]
    ways_of_payment: NotRequired[Any]


class State(TypedDict):
    created_at: NotRequired[str]
    end_date: NotRequired[str]
    registration_date: NotRequired[str]
    roles: NotRequired[List[str]]
    source: NotRequired[str]


class PostTerminal(TypedDict):
    address: NotRequired[str]
    created_at: NotRequired[str]
    end_date: NotRequired[str]
    id: NotRequired[int]
    identifier: NotRequired[str]
    jurisdiction: NotRequired[str]
    name: NotRequired[str]
    source: NotRequired[str]
    start_date: NotRequired[str]
    updated_at: NotRequired[str]


class Domain(TypedDict):
    city: NotRequired[str]
    contacts: NotRequired[List[str]]
    country: NotRequired[str]
    current_registar: NotRequired[str]
    domain_created: NotRequired[str]
    domain_name: NotRequired[str]
    domain_status: NotRequired[str]
    email_address: NotRequired[str]
    entities: NotRequired[List[str]]
    fax_number: NotRequired[str]
    last_modified: NotRequired[str]
    name: NotRequired[str]
    nic_handle: NotRequired[str]
    organization_name: NotRequired[str]
    phone_number: NotRequired[str]
    postal_code: NotRequired[str]
    primary_ip_address: NotRequired[str]
    primary_server: NotRequired[str]
    registar_created: NotRequired[str]
    secondary_ip_address: NotRequired[str]
    secondary_server: NotRequired[str]
    social_networks: NotRequired[List[str]]
    state: NotRequired[str]
    street_address: NotRequired[str]
    title: NotRequired[str]
    upload_id: NotRequired[Any]


class ScoringItem(TypedDict):
    bad_rate: NotRequired[float]
    created_at: NotRequired[str]
    group: NotRequired[str]
    id: NotRequired[int]
    identifier: NotRequired[str]
    jurisdiction: NotRequired[str]
    name: NotRequired[str]
    retrieved_at: NotRequired[str]
    score: NotRequired[float]
    updated_at: NotRequired[str]


class GovLoan(TypedDict):
    bank_name: NotRequired[str]
    created_at: NotRequired[str]
    desc: NotRequired[str]
    end_date: NotRequired[str]
    financing_source: NotRequired[str]
    guarantee_amount: NotRequired[float]
    id: NotRequired[int]
    identifier: NotRequired[str]
    loan_amount: NotRequired[float]
    loan_rate: NotRequired[str]
    name: NotRequired[str]
    purpose: NotRequired[str]
    start_date: NotRequired[str]
    updated_at: NotRequired[str]


class Trademark(TypedDict):
    application_date: NotRequired[str]
    application_number: NotRequired[str]
    bulletin_date: NotRequired[str]
    bulletin_number: NotRequired[str]
    classifications: NotRequired[List[str]]
    exp_date: NotRequired[str]
    holder: NotRequired[str]
    pdf_url: NotRequired[str]
    reg_date: NotRequired[str]
    reg_number: NotRequired[str]
    source_url: NotRequired[str]
    trademark_name: NotRequired[str]


class Counterparty(TypedDict):
    customer_identifier: NotRequired[str]
    customer_name: NotRequired[str]
    source: NotRequired[str]
    supplier_identifier: NotRequired[str]
    supplier_name: NotRequired[str]


class KaspiShop(TypedDict):
    cities: NotRequired[str]
    identifier: NotRequired[str]
    jurisdiction: NotRequired[str]
    phone: NotRequired[str]
    products: NotRequired[int]
    reviews: NotRequired[int]
    shop_id: NotRequired[str]
    shop_name: NotRequired[str]
    source: NotRequired[str]
    source_url: NotRequired[str]


class Asset(TypedDict):
    type: NotRequired[str]


class Right(TypedDict):
    application_date: NotRequired[str]
    company_id: NotRequired[int]
    holders: NotRequired[List[str]]
    name: NotRequired[str]
    object_date: NotRequired[str]
    object_type: NotRequired[str]
    person_name: NotRequired[str]
    registration_date: NotRequired[str]
    registration_number: NotRequired[str]
    status: NotRequired[str]


class ListOfData(TypedDict):
    registrations: NotRequired[List[Registration]]
    farmers: NotRequired[List[Farmer]]
    conf_certs: NotRequired[List[ConfCert]]
    excises: NotRequired[List[Excise]]
    bank_accounts: NotRequired[List[BankAccount]]
    stores: NotRequired[List[Store]]
    certs: NotRequired[List[Cert]]
    debtors: NotRequired[List[Debtor]]
    jobs: NotRequired[List[Job]]
    quasi_contracts: NotRequired[List[QuasiContract]]
    places: NotRequired[List[Place]]
    states: NotRequired[List[State]]
    post_terminals: NotRequired[List[PostTerminal]]
    domains: NotRequired[List[Domain]]
    scoring: NotRequired[List[ScoringItem]]
    gov_loans: NotRequired[List[GovLoan]]
    trademarks: NotRequired[List[Trademark]]
    counterparties: NotRequired[List[Counterparty]]
    kaspi_shops: NotRequired[List[KaspiShop]]
    assets: NotRequired[List[Asset]]
    rights: NotRequired[List[Right]]
    assets_count: NotRequired[int]
    bank_accounts_count: NotRequired[int]
    certs_count: NotRequired[int]
    counterparties_count: NotRequired[int]
    debtors_count: NotRequired[int]
    domains_count: NotRequired[int]
    farmers_count: NotRequired[int]
    fields_count: NotRequired[int]
    gov_loans_count: NotRequired[int]
    jobs_count: NotRequired[int]
    kaspi_count: NotRequired[int]
    places_count: NotRequired[int]
    pos_terminals_count: NotRequired[int]
    quasi_contracts_count: NotRequired[int]
    rights_count: NotRequired[int]
    scoring_count: NotRequired[int]
    states_count: NotRequired[int]
    stores_count: NotRequired[int]
    trademarks_count: NotRequired[int]
    excises_count: NotRequired[int]
    conf_certs_count: NotRequired[int]


class State1(TypedDict):
    state: NotRequired[str]
    total: NotRequired[int]


class Event(TypedDict):
    jurisdiction: NotRequired[str]
    date: NotRequired[str]
    attr: NotRequired[str]
    before: NotRequired[str]
    after: NotRequired[str]


class EventsWithMeta(TypedDict):
    events: NotRequired[List[Event]]


class Company(TypedDict):
    id: NotRequired[int]
    identifier: NotRequired[str]
    name: NotRequired[str]
    name_en: NotRequired[str]


class SubsidiariesCompanyWithMeta(TypedDict):
    companies: NotRequired[List[Company]]
    total: NotRequired[int]
    pagination_count: NotRequired[int]
    pagination_offset: NotRequired[int]


class NodeItem(TypedDict):
    id: NotRequired[int]
    name: NotRequired[str]
    type: NotRequired[str]
    is_person: NotRequired[bool]
    key: NotRequired[str]


class Link1(TypedDict):
    id: NotRequired[int]
    name: NotRequired[str]
    source_key: NotRequired[int]
    type: NotRequired[str]
    connection_type: NotRequired[str]
    connection_id: NotRequired[int]
    connection_name: NotRequired[str]
    connection_hash_identifier: NotRequired[str]
    connection_key: NotRequired[int]
    is_person: NotRequired[bool]


class MetaItem1(TypedDict):
    name: NotRequired[int]


class RelationResult(TypedDict):
    node: NotRequired[List[NodeItem]]
    links: NotRequired[List[Link1]]
    meta: NotRequired[List[MetaItem1]]
    total: NotRequired[int]


class SocialNetwork(TypedDict):
    name: NotRequired[str]
    account_name: NotRequired[str]
    identifier: NotRequired[str]
    description: NotRequired[str]
    url: NotRequired[str]
    email: NotRequired[str]
    website: NotRequired[str]
    jurisdiction: NotRequired[str]
    matched_contact: NotRequired[List[str]]


SocialNetworks = List[SocialNetwork]


class TaxDeclaration(TypedDict):
    amount: NotRequired[float]
    doc_type: NotRequired[str]
    doc_num: NotRequired[str]
    date: NotRequired[str]


class TaxDeclarationsResult(TypedDict):
    tax_regime: NotRequired[str]
    tax_declarations: NotRequired[List[TaxDeclaration]]


class Event1(TypedDict):
    status: NotRequired[str]
    date: NotRequired[str]


class CourtCase(TypedDict):
    external_id: str
    case_number: str
    instance: NotRequired[str]
    case_type: NotRequired[str]
    start_date: NotRequired[str]
    end_date: NotRequired[str]
    court: str
    category: NotRequired[str]
    judge: NotRequired[str]
    sides: NotRequired[List[str]]
    defendants: NotRequired[List[str]]
    plaintiffs: NotRequired[List[str]]
    result: NotRequired[str]
    events: NotRequired[List[Event1]]
    jurisdiction: str


class CourtCasesMetaItem(TypedDict):
    type: str
    total: int


CourtCasesMeta = List[CourtCasesMetaItem]


class Employee(TypedDict):
    identifier: NotRequired[str]
    name: NotRequired[str]
    position: NotRequired[str]
    employer_identifier: NotRequired[str]
    employer_name: NotRequired[str]
    employer_jurisdiction: NotRequired[str]
    created_at: NotRequired[str]
    updated_at: NotRequired[str]
    start_date: NotRequired[str]
    end_date: NotRequired[str]


class TypeTotal(TypedDict):
    type: NotRequired[str]
    total: NotRequired[int]


class EmployeesWithMeta(TypedDict):
    employees: NotRequired[List[Employee]]
    total: NotRequired[int]
    type_total: NotRequired[TypeTotal]
    pagination_count: NotRequired[int]
    pagination_offset: NotRequired[int]


class Identifier5(TypedDict):
    type: str
    value: NotRequired[str]


class MainIndustryCode2(TypedDict):
    code: str
    description: NotRequired[str]
    is_main: bool


class Capital(TypedDict):
    share_capital: NotRequired[float]
    paid_up_capital: NotRequired[float]
    currency: NotRequired[str]


class Branch(TypedDict):
    id: NotRequired[int]
    name: NotRequired[str]
    name_en: NotRequired[str]


class Name(TypedDict):
    name: str


class Address1(TypedDict):
    raw: str
    state: NotRequired[str]
    path: str


Addresses = List[Address1]


class Contact1(TypedDict):
    id: int
    type: str
    value: str


Contacts = List[Contact1]


class Accrual(TypedDict):
    kbk: NotRequired[str]
    paid: NotRequired[float]
    year: NotRequired[int]


class Financial(TypedDict):
    year: NotRequired[int]
    taxes: NotRequired[float]
    net_profit: NotRequired[float]
    revenue: NotRequired[float]
    accruals: NotRequired[List[Accrual]]


Financials = List[Financial]


class HeadcountItem(TypedDict):
    count: NotRequired[str]
    date: NotRequired[str]


Headcount = List[HeadcountItem]


class Record1(TypedDict):
    k: str
    v: str


class Record(TypedDict):
    object: str
    desc: str
    records: NotRequired[List[Record1]]


class Risk(TypedDict):
    status: str
    object: str
    source: str
    records: NotRequired[List[Record]]


Risks = List[Risk]


class IndustryCode(TypedDict):
    code: str
    description: NotRequired[str]
    is_main: bool


IndustryCodes = List[IndustryCode]


class Contact2(TypedDict):
    id: int
    value: str


class Record2(TypedDict):
    k: str
    v: str


class Records(TypedDict):
    object: str
    desc: str
    records: NotRequired[List[Record2]]


class Risk1(TypedDict):
    status: str
    object: str
    source: str
    records: NotRequired[Union[List[Dict[str, Any]], Records]]


class Officer1(TypedDict):
    identifier: NotRequired[str]
    name: str
    name_en: str
    name_native: NotRequired[str]
    role: NotRequired[str]
    start_date: NotRequired[str]
    end_date: NotRequired[str]
    inactive: bool
    contacts: NotRequired[List[Contact2]]
    risks: NotRequired[List[Risk1]]
    hash_bin: str


Officers = List[Officer1]


class Record3(TypedDict):
    object: str
    desc: str
    records: NotRequired[List[Record2]]


class Risk2(TypedDict):
    status: NotRequired[str]
    object: NotRequired[str]
    source: NotRequired[str]
    records: NotRequired[List[Record3]]


class Shareholder(TypedDict):
    shareholder_company_id: int
    identifier: NotRequired[str]
    name: str
    name_en: str
    name_native: str
    role: NotRequired[str]
    is_person: bool
    share: NotRequired[int]
    share_capital: NotRequired[int]
    start_date: NotRequired[str]
    end_date: NotRequired[str]
    inactive: NotRequired[bool]
    contacts: NotRequired[List[Contact2]]
    risks: NotRequired[List[Risk2]]
    hash_bin: str


Shareholders = List[Shareholder]


class Alternative(TypedDict):
    id: NotRequired[int]
    identifier: NotRequired[str]
    title: NotRequired[str]
    name: NotRequired[str]
    name_en: NotRequired[str]
    company_size: NotRequired[str]
    jurisdiction: NotRequired[str]
    industry: NotRequired[str]
    industry_code: NotRequired[str]
    main_industry_code: NotRequired[MainIndustryCode2]
    source_inactive: NotRequired[bool]


Alternatives = List[Alternative]


class RisksMetaData(TypedDict):
    company: NotRequired[Risks]
    shareholders: NotRequired[Risks]
    officers: NotRequired[Risks]


class Seo(TypedDict):
    title: NotRequired[str]
    description: NotRequired[str]
    keywords: NotRequired[str]


class ResultContacts(TypedDict):
    website: NotRequired[Contacts]
    phone: NotRequired[Contacts]
    email: NotRequired[Contacts]


class RelationsMetaItem(TypedDict):
    connection: str
    count: int


RelationsMeta = List[RelationsMetaItem]


class ViewMetaBeta(TypedDict):
    events: NotRequired[int]
    employment_contracts: NotRequired[int]
    subsidiaries: NotRequired[int]
    contacts: NotRequired[int]


class Error(TypedDict):
    error: int
    message: str


class UsersLinkedCompany(TypedDict):
    id: NotRequired[int]
    identifier: NotRequired[str]
    title: NotRequired[str]
    name: NotRequired[str]
    name_en: NotRequired[str]
    name_native: NotRequired[str]
    company_size: NotRequired[str]
    jurisdiction: NotRequired[str]
    inactive: NotRequired[bool]
    addresses: NotRequired[Addresses]
    contacts: NotRequired[Contacts]
    identifiers: NotRequired[List[Identifier]]
    main_industry_code: NotRequired[List[MainIndustryCodeItem]]
    industry_codes: NotRequired[List[IndustryCodes]]
    officers: NotRequired[Officers]
    shareholders: NotRequired[Shareholders]
    risks: NotRequired[Risks]
    last_update_date: NotRequired[str]
    dissolution_date: NotRequired[str]
    incorporation_date: NotRequired[str]
    structure: NotRequired[str]
    deleted_at: NotRequired[str]


UsersLinkedCompanies = List[UsersLinkedCompany]


class CompanyItem(TypedDict):
    id: NotRequired[int]
    identifier: NotRequired[str]
    title: NotRequired[str]
    name: NotRequired[str]
    name_en: NotRequired[str]
    name_native: NotRequired[str]
    company_size: NotRequired[str]
    jurisdiction: NotRequired[str]
    industry: NotRequired[str]
    inactive: NotRequired[bool]
    addresses: NotRequired[Addresses]
    headcount: NotRequired[Headcount]
    identifiers: NotRequired[List[Identifier]]
    industry_codes: NotRequired[IndustryCodes]
    main_industry_code: NotRequired[MainIndustryCode]
    officers: NotRequired[Officers]


class CompaniesByMainIndustryCode(TypedDict):
    company: NotRequired[List[CompanyItem]]
    total: NotRequired[int]
    pagination_total: NotRequired[int]
    pagination_offset: NotRequired[int]


class Busines(TypedDict):
    id: NotRequired[int]
    identifier: NotRequired[str]
    title: NotRequired[str]
    name: NotRequired[str]
    name_en: NotRequired[str]
    name_native: NotRequired[str]
    company_size: NotRequired[str]
    jurisdiction: NotRequired[str]
    industry: NotRequired[str]
    status: NotRequired[str]
    ownership_type: NotRequired[str]
    inactive: NotRequired[bool]
    addresses: NotRequired[Addresses]
    headcount: NotRequired[Headcount]
    industry_codes: NotRequired[IndustryCodes]
    officers: NotRequired[List[Officer]]
    structure: NotRequired[str]
    view_date: NotRequired[str]


class ReportsHistory(TypedDict):
    business: NotRequired[List[Busines]]
    total: NotRequired[int]
    pagination_count: NotRequired[int]
    pagination_offset: NotRequired[int]


class Item(TypedDict):
    id: NotRequired[int]
    company_id: NotRequired[int]
    company_name: NotRequired[str]
    industry: NotRequired[str]
    jurisdiction: NotRequired[str]
    addresses: NotRequired[Addresses]
    headcount: NotRequired[Headcount]
    officers: NotRequired[Officers]
    identifiers: NotRequired[List[Identifier2]]
    created_at: NotRequired[str]
    deleted_at: NotRequired[str]


class FavouriteObjectResponse(TypedDict):
    pagination_offset: NotRequired[int]
    pagination_total: NotRequired[int]
    items: NotRequired[List[Item]]


class IndividualPersonWithData(TypedDict):
    name: NotRequired[str]
    name_en: NotRequired[str]
    identifier: NotRequired[str]
    jurisdiction: NotRequired[str]
    contacts: NotRequired[List[Contact]]
    risks: NotRequired[Risks]
    shareholders: NotRequired[Alternatives]
    officers: NotRequired[Alternatives]
    meta: NotRequired[Meta]
    is_full: NotRequired[bool]


class CompanyItem2(TypedDict):
    id: NotRequired[int]
    identifier: NotRequired[str]
    title: NotRequired[str]
    name: NotRequired[str]
    name_en: NotRequired[str]
    name_native: NotRequired[str]
    company_size: NotRequired[str]
    jurisdiction: NotRequired[str]
    industry: NotRequired[str]
    inactive: NotRequired[bool]
    addresses: NotRequired[Addresses]
    headcount: NotRequired[Headcount]
    identifiers: NotRequired[List[Identifier3]]
    industry_codes: NotRequired[IndustryCodes]
    main_industry_code: NotRequired[MainIndustryCode]
    officers: NotRequired[Officers]


class CompanyWithState(TypedDict):
    company: NotRequired[List[CompanyItem2]]
    state: NotRequired[State1]
    count: NotRequired[int]
    pagination_count: NotRequired[int]
    pagination_offset: NotRequired[int]


class CourtCaseResult(TypedDict):
    court_cases: NotRequired[List[CourtCase]]
    case_type_meta: NotRequired[CourtCasesMeta]
    meta: NotRequired[CourtCasesMeta]
    year_meta: NotRequired[CourtCasesMeta]
    total: NotRequired[int]


CompanyModel = TypedDict(
    "CompanyModel",
    {
        "id": NotRequired[int],
        "identifier": NotRequired[str],
        "title": NotRequired[str],
        "name": NotRequired[str],
        "name_en": NotRequired[str],
        "name_native": NotRequired[str],
        "legal_form": NotRequired[str],
        "company_size": NotRequired[str],
        "jurisdiction": NotRequired[str],
        "industry": NotRequired[str],
        "status": NotRequired[str],
        "ownership_type": NotRequired[str],
        "var_payer": NotRequired[bool],
        "inactive": NotRequired[bool],
        "addresses": NotRequired[Addresses],
        "contacts": NotRequired[Contacts],
        "financials": NotRequired[Financials],
        "headcount": NotRequired[Headcount],
        "identifiers": NotRequired[List[Identifier5]],
        "main_industry_code": NotRequired[MainIndustryCode2],
        "industry_codes": NotRequired[IndustryCodes],
        "officers": NotRequired[Officers],
        "shareholders": NotRequired[Shareholders],
        "risks": NotRequired[Risks],
        "capital": NotRequired[Capital],
        "managing_company_id": NotRequired[int],
        "managing_company_name": NotRequired[str],
        "branches": NotRequired[List[Branch]],
        "names": NotRequired[List[Name]],
        "export": NotRequired[List[str]],
        "import": NotRequired[List[str]],
        "last_update_date": NotRequired[str],
        "dissolution_date": NotRequired[str],
        "incorporation_date": NotRequired[str],
        "created_at": NotRequired[str],
        "updated_at": NotRequired[str],
        "structure": NotRequired[str],
    },
)


class CompanyResult(TypedDict):
    company: NotRequired[CompanyModel]
    alternatives: NotRequired[Alternatives]
    is_full: bool
    risks_meta_data: NotRequired[RisksMetaData]
    contacts: NotRequired[ResultContacts]
    seo: NotRequired[Seo]


class CompanyBetaResult(TypedDict):
    company: NotRequired[CompanyModel]
    alternatives: NotRequired[Alternatives]
    risks_meta_data: NotRequired[RisksMetaData]
    seo: NotRequired[Seo]
    relations: NotRequired[RelationsMeta]
    meta: NotRequired[ViewMetaBeta]
