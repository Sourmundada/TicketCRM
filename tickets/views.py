from django.shortcuts import redirect, render, get_object_or_404
from accounts.models import Account, Staff
from .models import Attachment, Ticket
from .forms import TicketForm, AttachmentForm
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'tickets/index.html')

@login_required(login_url='admin_login')
def admin_home(request):
    staff = Staff.objects.all().order_by('-last_login')
    tickets = Ticket.objects.all()
    

    context = {
        'staff': staff,
        'tickets': tickets,
    }

    return render(request, 'owner/admin_home.html', context=context)

@login_required(login_url='staff_login')
def staff_home(request):
    if request.user.is_admin:
        return redirect('admin_home')
    else:
        tickets = Ticket.objects.filter(assigned_to=request.user)
    return render(request, 'staff/staff_home.html', {'tickets': tickets})

@login_required(login_url='index')
def add_tickets(request):
    if request.user.is_admin:
        if request.method == "POST":
            form = TicketForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('admin_home')
            else:
                return redirect('index')
    else:
        return redirect('index')
    
    return render(request, 'tickets/add_ticket.html', {'form': TicketForm()})

@login_required(login_url='index')
def update_ticket(request, ticket_pk):
    if request.user.is_admin:
        ticket = get_object_or_404(Ticket, id=ticket_pk)
        if request.method == "POST":
            form = TicketForm(request.POST, instance=ticket)
            if form.is_valid():
                form.save()
                return redirect('admin_home')
            else:
                return redirect('index')
    else:
        return redirect('index')
    
    return render(request, 'tickets/update_ticket.html', {'form': TicketForm(instance=ticket)})

@login_required(login_url='staff_login')
def view_ticket(request, ticket_pk):
    
    ticket = get_object_or_404(Ticket, id=ticket_pk)

    attachments = Attachment.objects.filter(ticket=ticket)
    attachments_count = attachments.count()

    if request.method == "POST":
        ticket.status = request.POST['status']
        ticket.save()
        return redirect('index')

    return render(request, 'tickets/view_ticket.html', {'ticket': ticket, 'attachments': attachments, 'attachments_count': attachments_count})

@login_required(login_url='index')
def delete_ticket(request, ticket_pk):
    if request.user.is_admin:
        ticket = get_object_or_404(Ticket, id=ticket_pk)
        if request.method == "POST":
            ticket.delete()
            return redirect('admin_home')
    else:
        return redirect('index')

    return render(request, 'tickets/view_ticket.html')

@login_required(login_url='index')
def staff_tickets(request, user_pk):

    if request.user.is_admin:
        staff_user = get_object_or_404(Staff, id=user_pk)

        tickets = Ticket.objects.filter(assigned_to=staff_user)
        tickets_count = tickets.count()

        if request.method == "POST":
            if staff_user.is_active == True:
                staff_user.is_active = False
                staff_user.save()
            else:
                staff_user.is_active = True
                staff_user.save()
            return redirect('admin_home')
    else:
        return redirect('index')

    return render(request, 'tickets/staff_tickets.html', {'staff_user': staff_user, 'tickets': tickets, 'tickets_count': tickets_count})


@login_required(login_url='index')
def add_attachments(request):
    if request.user.is_admin:
        if request.method == "POST":
            form = AttachmentForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('admin_home')
            else:
                return redirect('index')
    else:
        return redirect('index')
    
    return render(request, 'tickets/attachments.html', {'form': AttachmentForm()})