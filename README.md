# Education Certificate Management

## Overview

**Education Certificate Management** is an Odoo module that provides a complete certificate issuance system for educational institutions. It allows administrators to create, issue, print, and manage certificates for students, faculty members, and employees.

The module supports certificate numbering, QR code generation, digital signatures, certificate templates, and certificate type management.

---

## Features

### Certificate Management

* Create certificates with automatic certificate numbering.
* Support for multiple recipient types:

  * Student
  * Faculty
  * Employee
* Certificate status workflow:

  * Draft
  * Issued
  * Cancelled
* Certificate issue and expiry dates.
* Achievement or description section.

### Certificate Types

* Manage different certificate categories.
* Define type code and sequence.
* Archive unused certificate types.
* Unique certificate type validation.

### Digital Signature Support

* Select signatory from Employees.
* Only employees having a signature image can be selected.
* Signature automatically appears on the printed certificate.

### QR Code Generation

* QR code generated automatically from certificate number.
* QR code printed on certificate.
* Easy verification and authenticity support.

### PDF Certificate Printing

* Professional certificate layout.
* Certificate title and recipient information.
* Rich text certificate content.
* Signature section.
* QR code section.
* Certificate number.
* Issue date display.

### Communication Features

* Chatter integration.
* Followers support.
* Activities support.
* Message tracking.

---

## Models

### certificate.issued

Stores issued certificates.

#### Main Fields

* certificate_number
* name
* recipient_type
* student_id
* faculty_id
* employee_id
* recipient_name
* certificate_type_id
* issue_date
* expiry_date
* description
* signatory_id
* qr_code
* state

---

### certificate.type

Stores certificate categories.

#### Main Fields

* name
* code
* sequence
* description
* active

---

## Workflow

```
Create Certificate
        ↓
Select Recipient Type
        ↓
Choose Recipient
        ↓
Select Certificate Type
        ↓
Write Description
        ↓
Select Signatory
        ↓
Save Record
        ↓
Issue Certificate
        ↓
Generate QR Code
        ↓
Print PDF Certificate
```

---

## Automatic Certificate Number

Format:

```
CERT/00001
CERT/00002
CERT/00003
...
```

Sequence Code:

```
certificate.issued
```

Prefix:

```
CERT/
```

Padding:

```
5
```

---

## Menu Structure

```
Certificates
│
├── Certificate Types
│
└── Issued Certificates
```

---

## Dependencies

```python
mail
hr
```

Additional models used:

* education.student
* education.faculty
* hr.employee

---

## Technical Features

### QR Code Generation

Uses:

```python
qrcode
base64
BytesIO
```

QR code is generated automatically from:

```python
certificate_number
```

---

### Report

Report Type:

```python
qweb-pdf
```

Report ID:

```python
action_certificate_report
```

Template:

```python
education_certificate_management.certificate_report_template
```

---

## Installation

1. Copy module into custom addons directory.

```bash
custom_addons/
└── education_certificate_management
```

2. Restart Odoo.

```bash
sudo systemctl restart odoo
```

3. Update Apps List.

4. Install:

```
Education Certificate Management
```

---

## Usage

### Create Certificate

Certificates → Issued Certificates → New

1. Enter Certificate Title.
2. Select Recipient Type.
3. Choose Student / Faculty / Employee.
4. Select Certificate Type.
5. Write achievement details.
6. Select Signatory.
7. Save.
8. Click **Issue Certificate**.
9. Print PDF.

---

## Author

Kendroo LTD
## Version

1.0

## License

LGPL-3
