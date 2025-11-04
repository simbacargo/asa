from django.shortcuts import render

def index(req):
    return render(req, "base.html")

def about(req):
    return render(req, "about.html")

def services(req):
    return render(req, "services.html")

def regional_reach(req):
    return render(req, "regional_reach.html")

def contact(req):
    return render(req, "contact.html")

def logistics(req):
    return render(req, "logistics.html")

def ShipBroking(req):
    return render(req, "ShipBroking.html")

def VesselAgency(req):
    return render(req, "VesselAgency.html")

def quote_request(req):
    return render(req, "quote_request.html")
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_POST
import logging

# Set up logging for demonstration
logger = logging.getLogger(__name__)

# The @require_POST decorator ensures this view only accepts POST requests, 
# which is perfect for form submissions like this.
@require_POST
def quote_request_view(request):
    """
    Handles the POST request from the HTMX quote submission form.
    Processes the form data and returns an HTML fragment to replace the form container.
    """
    
    # 1. Extract Data
    full_name = request.POST.get('full_name', '')
    email = request.POST.get('email', '')
    phone = request.POST.get('phone', '')
    service_interest = request.POST.get('service_interest', '')
    details = request.POST.get('details', '')
    
    # 2. Basic Validation (Django forms are recommended for complex validation)
    if not all([full_name, email, service_interest, details]):
        # If validation fails, you would typically re-render the form with error messages.
        # For simplicity in this HTMX example, we'll return a simple error fragment.
        error_message = """
            <div id="form-container" class="bg-red-50 p-8 sm:p-12 rounded-2xl shadow-2xl border-t-2 border-red-500 text-red-800 text-center">
                <p class="text-xl font-bold mb-3">Submission Failed!</p>
                <p>Please ensure all required fields are filled out.</p>
                <!-- In a real app, you might include a button here to re-display the form -->
            </div>
        """
        return HttpResponse(error_message, status=400) # 400 Bad Request

    # 3. Process Data (e.g., Save to Database, Send Email Notification)
    
    # --- SIMULATION ---
    # In a real application, you would:
    # 1. Save the quote request object to your database (e.g., QuoteRequest.objects.create(...))
    # 2. Trigger an email notification to the relevant team.
    
    logger.info(f"--- NEW QUOTE REQUEST RECEIVED ---")
    logger.info(f"Name: {full_name}, Email: {email}, Phone: {phone}")
    logger.info(f"Service: {service_interest}")
    logger.info(f"Details: {details[:50]}...") # Log first 50 chars of details
    # ------------------

    # 4. Return HTMX Success Fragment
    
    # This HTML snippet replaces the entire <div id="form-container"> as requested by hx-swap="outerHTML"
    success_html = f"""
        <div id="form-container" class="p-8 bg-green-50 border-t-2 border-green-600 text-green-900 rounded-2xl shadow-xl transition-opacity duration-1000 opacity-100">
            <p class="text-3xl font-extrabold mb-4 flex items-center">
                <svg class="w-8 h-8 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                Request Submitted Successfully, {full_name.split()[0]}!
            </p>
            <p class="text-lg text-gray-700">
                Thank you for reaching out to Access Shipping Agency. We have received your detailed quote request and a dedicated logistics specialist will contact you directly within 24 hours.
            </p>
        </div>
    """
    
    # Return the success message to replace the form.
    return HttpResponse(success_html)

# Add dummy views for the service tabs to prevent 404s when the user clicks them
def service_detail_view(request, service_id):
    """
    Placeholder view for handling the HTMX GET requests for service tabs 
    (e.g., /services/port-agency).
    In a real app, this would query the DB or render a specific service template.
    """
    
    # Get the mock content logic (adapted to Django context)
    details_map = {
        'port-agency': 'Full Vessel Agency, Owners\' Protective Agents, Cargo Agents, Supervisory Agents, Charterers Agents, and Liner Agencies. We offer 24/7 support for all your vessel\'s needs, ensuring fast turnaround times.',
        'logistics': 'Seamless supply chain solutions from customs clearance to distribution. We handle FCL, LCL, break bulk, bulk, and project cargo across East Africa.',
        'broking': 'Expert ship broking, chartering (focused on time charter projects), and comprehensive consulting services covering maritime, financial, and supply chain strategies.',
        'crew': 'Providing highly trained, hardworking East African seafarers. Our services include screening, training, document control, medical checks, and full crew change planning.',
    }
    
    content_map = {
        'port-agency': """
            <ul class="list-disc ml-6 space-y-3 text-gray-700 font-medium">
                <li><span class="asa-blue-text font-bold">Crew Handling:</span> 24/7 Crew Changes & Spare Parts Logistics</li>
                <li><span class="asa-blue-text font-bold">Supply Chain:</span> Provisioning, Freshwater, and Bunkers Supply</li>
                <li><span class="asa-blue-text font-bold">Vessel Coverage:</span> Tankers, Bulk Carriers, Liners, Cruise Ships, Navy Vessels.</li>
            </ul>
        """,
        'logistics': """
            <div class="space-y-4">
                <h4 class="text-xl font-extrabold asa-blue-text">Logistics Modalities:</h4>
                <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
                    <div class="p-4 bg-gray-100 rounded-xl shadow-md text-center font-semibold text-gray-800 border-b-4 border-yellow-500">Road & Rail Transport</div>
                    <div class="p-4 bg-gray-100 rounded-xl shadow-md text-center font-semibold text-gray-800 border-b-4 border-yellow-500">Air Freight & Charters</div>
                    <div class="p-4 bg-gray-100 rounded-xl shadow-md text-center font-semibold text-gray-800 border-b-4 border-yellow-500">Secure Bonded Warehousing</div>
                    <div class="p-4 bg-gray-100 rounded-xl shadow-md text-center font-semibold text-gray-800 border-b-4 border-yellow-500">Customs Clearance Expertise</div>
                </div>
            </div>
        """,
        'broking': """
            <div class="p-4 bg-blue-50 border-t-2 border-asa-blue rounded-xl text-gray-800">
                <p class="font-bold text-lg mb-2">Maritime Advisory:</p>
                <ul class="list-disc ml-6 space-y-1">
                    <li>Cargo Forecasting & Market Feasibility Studies</li>
                    <li>Vessel Inspection, Repairs, and Quality Assurance</li>
                    <li>Customs Law & Procedures Consultancy in East Africa</li>
                </ul>
            </div>
        """,
        'crew': """
            <div class="p-6 bg-yellow-50 border-t-2 border-yellow-500 rounded-xl text-yellow-800">
                <p class="font-bold text-xl mb-1">Seafarer Excellence:</p>
                <p>We source and manage professional seafarers, assisting with all immigration, customs, and transportation logistics for crew changes, ensuring full compliance.</p>
            </div>
        """,
    }

    details = details_map.get(service_id, 'Select a service above to see detailed information.')
    content = content_map.get(service_id, '<p class="text-gray-500 italic">No content selected.</p>')
    
    response_content = f"""
        <div class="p-6 bg-white rounded-2xl shadow-2xl transition-all duration-300 transform scale-100">
            <p class="text-xl font-semibold text-gray-700 mb-6">{details}</p>
            {content}
        </div>
    """
    
    return HttpResponse(response_content)
